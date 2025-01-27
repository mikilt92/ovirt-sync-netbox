import csv
import urllib3
import sys
import os

# Disable warnings related to expired SSL certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import config

# Use variables from config.py
NETBOX_URL = config.NETBOX_URL
NETBOX_TOKEN = config.NETBOX_TOKEN

# Main function to process the CSV file
def main():
    files = [
        "exported_info/hosts_info.csv",
    ]
    for file in files:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if file == "exported_info/hosts_info.csv":
                for row in reader:
                    data = {
                        "name": row['name'],
                        "role": row['role'],
                        "tenant": row['tenant'],
                        "manufacturer": row['manufacturer'],
                        "device_type": row['device_type'],
                        "platform": row['platform'],
                        "serial": row['serial'],
                        "status": row['status'],
                        "site": row['site'],
                        "cluster": row['cluster'],
                        "tags": row['tags'],
                        "vcsa_host_memory": row['cf_vcsa_host_memory']
                        # Add other fields if necessary
                    }
                    host_id = config.get_hosts_id(data["name"])
                    if host_id is None:
                        config.create_host(data)
                    else:
                        config.update_host(host_id,data)

if __name__ == "__main__":
    main()
