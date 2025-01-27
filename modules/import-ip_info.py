import csv
import requests
import urllib3
import sys
import os
import requests

# Disable warnings related to expired SSL certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import config

# Use variables from config.py
NETBOX_URL = config.NETBOX_URL
NETBOX_TOKEN = config.NETBOX_TOKEN

# Main function to process the CSV file
def main():
    file_path = "exported_info/ip_info.csv"  # Enter the correct path to your CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if mandatory fields are not empty before processing
            if row['address'] and row['tenant'] and row['tags']:
                # Build the data dictionary including only non-empty fields
                data = {
                    "address": row['address'],
                    "tenant": row['tenant'],
                    "tags": row['tags'],
                    "mac_address": row['mac_address'],
                    "virtual_machine": row['virtual_machine'], 
                    "status": row['status']
                }
                tag_id = config.get_tag_id(data["tags"])
                vm_info = config.get_vm_info(data["virtual_machine"],tag_id)
                vm_id = vm_info["id"] 
                tenant_id = config.get_tenant_id(data['tenant'])
                if tenant_id is None:
                    tenant_id = config.create_tenant(data['tenant'])
                interface_id = config.get_interface_id_by_mac(data['virtual_machine'], data['mac_address'])
                ip_info = config.get_ips(data['address'],vm_id,data['tags']) 

                if not ip_info:
                    # Call the function to create the IP address with the extracted data
                    config.create_ip_address(tenant_id,tag_id,interface_id,data)
                else:
                    ip_id = ip_info[0]['id']
                    config.update_ip_address(ip_id,tenant_id,tag_id,interface_id,data)

            else:
                print("One or more mandatory fields in the CSV file are empty and cannot be processed.")

if __name__ == "__main__":
    main()
