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
    file = "exported_info/vms.csv"  # Insert the correct path of your CSV file
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {
                "name": row['name'],
                "status": row['status'],
                "role": row['role'],
                "site": row['site'],
                "cluster": row['cluster'],
                "device": row['device'],
                "tenant": row['tenant'],
                "platform": row['platform'],
                "vcpus": int(row['vcpus']),
                "memory": int(row['memory']),
                "disk": int(row['disk']),
                "description": row['description'],
                "config_template": row['config_template'],
                "comments": row['comments'],
                "tags": row['tags']
                # Add other fields if necessary
            }
            tag_id = config.get_tag_id(data["tags"])
            vm_info = config.get_vm_info(data["name"],tag_id)
            if vm_info is None:
                config.create_vm(data)
            else:
                config.update_vm(vm_info["id"],data)

if __name__ == "__main__":
    main()