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
    file = "exported_info/nics_vms.csv"  # Insert the correct path of your CSV file
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if the mandatory fields are not empty before processing them
            if row['virtual_machine'] and row['name'] and row['tenant'] and row['tags']:
                # Check if optional fields are empty and set them to None if they are
                optional_fields = ['parent', 'bridge', 'enabled', 'mac_address', 'mtu', 'mode', 'vrf']
                for field in optional_fields:
                    if not row[field]:
                        row[field] = None

                # Check the 'description' field and set it to None if it's empty
                description = row['description'] if row['description'] else None

                # Build the data dictionary including only non-empty fields
                data = {
                    "name": row['name'],
                    "virtual_machine": row['virtual_machine'],
                    "tenant": row['tenant'],
                    "tags": row['tags']
                }

                # Add optional fields only if they are not empty
                if description:
                    data["description"] = description
                if row["mac_address"]:
                    data["mac_address"] = row["mac_address"]
                if row["enabled"]:
                    data["enabled"] = row["enabled"]
                if row["mtu"]:
                    data["mtu"] = int(row["mtu"])
                if row["mode"]:
                    data["mode"] = row["mode"]
                if row["vrf"]:
                    data["vrf"] = row["vrf"]
                
                tag_id = config.get_tag_id(data["tags"])
                vm_info = config.get_vm_info(data["virtual_machine"],tag_id)
                vm_id = vm_info["id"] 
                interface_id = config.get_nics(vm_id,data["name"])
            
                if interface_id is None:
                    config.create_interface(vm_id,data)
                else:
                    config.update_interface(interface_id,vm_id,data)
                    # config.update_interface()
            else:
                print("One or more mandatory fields in the CSV file are empty and cannot be processed.")

if __name__ == "__main__":
    main()