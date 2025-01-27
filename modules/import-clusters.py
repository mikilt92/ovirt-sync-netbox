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

# Main function to process different CSV files
def main():
    files = [
        "exported_info/clusters.csv",
    ]
    for file in files:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if file == "exported_info/clusters.csv":
                for row in reader:
                    data = {
                        "name": row['name'],
                        "type": row['type'],
                        "group": row['group'],
                        "status": row['status'],
                        "site": row['site'],
                        "tenant": row['tenant'],
                        "tags": row['tags']
                        # Add other fields if necessary
                    }
                    cluster_id = config.get_cluster_id(data["name"])
                    if cluster_id is None:
                        config.create_cluster(data)
                    else:
                        # print (f'{data["tags"]}')
                        config.update_cluster(cluster_id[0]["id"],data)

if __name__ == "__main__":
    main()