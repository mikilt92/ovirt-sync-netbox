import csv
import requests
import urllib3
import sys
import os
import requests
import re

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
        "exported_info/data_centers.csv",
    ]
    for file in files:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if file == "exported_info/data_centers.csv":
                for row in reader:
                    data = {
                        "name": row['name'],
                        "slug": row['slug'],
                        "tags": row['tags']
                        # Add other fields if necessary
                    }
                    clustergroups = config.get_clustergroups(data["name"])
                    if clustergroups is None:
                        config.create_clustergroups(data)
                    else:
                        config.update_clustergroups(clustergroups["id"],data)

if __name__ == "__main__":
    main()
