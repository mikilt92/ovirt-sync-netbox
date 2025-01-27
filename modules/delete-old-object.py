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

tag_slug = (config.tag.replace(" ", "").replace(":", "").lower())
# data["tags"].replace(" ", "").replace(":", "").lower(),tag_description)

devices_ids = config.get_old_devices(tag_slug)
for device_id in devices_ids:
    config.delete_devices(device_id)

interfaces_ids = config.get_old_interfaces(tag_slug)
for interface_id in interfaces_ids:
    config.delete_interfaces(interface_id)

vitual_machines_ids = config.get_old_virtual_machines(tag_slug)
for vitual_machine_id in vitual_machines_ids:
    config.delete_virtual_machines(vitual_machine_id)

clusters_ids = config.get_old_clusters(tag_slug)
for cluster_id in clusters_ids:
    config.delete_clusters(cluster_id)

cluster_groups_ids = config.get_old_cluster_groups(tag_slug)
for cluster_group_id in cluster_groups_ids:
    config.delete_cluster_groups(cluster_group_id)

ip_addresses_ids = config.get_old_ip_addresses(tag_slug)
for ip_addresses_id in ip_addresses_ids:
    config.delete_ip_addresses(ip_addresses_id)

platforms_id = config.get_old_platforms(tag_slug)
for platform_id in platforms_id:
    config.delete_platforms(platform_id)

