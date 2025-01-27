# config.py
import requests
import re
from datetime import datetime, timedelta


# Settings for access to Netbox
NETBOX_URL = "https://NETBOXURL"
NETBOX_TOKEN = "NETBOX_TOKEN"

# Setting for access to oVirt
host_fqdn = 'OVIRT_FQDN'

# Global variables
type = 'oVirt'
site = 'oVirt_Site'
tenant = 'oVirt_Tenant'
tag = 'Source: oVirt'
vm_role = 'Server'
tag_description = f'Marks objects synced from oVirt "{host_fqdn}" to this NetBox Instance.'
days_rentention = 30

# Functions to get the Objects ID

# Function to get all devices with {tag}
def get_old_devices(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    device_url = NETBOX_URL + f"api/dcim/devices/?tag={tag_slug}"

    all_devices = []

    while device_url:
        response = requests.get(device_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            devices = data["results"]
            for device in devices:
                device_id = device["id"]
                device_name = device["name"]
                device_last_updated = device["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(device_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    # tags = device.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]  
                    print(f"The device {device_name} has this ID {device_id} and the last update was {device_last_updated}")
                    all_devices.append((device_id))
                
            device_url = data["next"]
        else:
            print("Error while fetching devices from Netbox.")
            print(response.text)
            return None

    return all_devices

# Function to get all virtual interfaces with {tag}
def get_old_interfaces(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    interface_url = NETBOX_URL + f"api/virtualization/interfaces/?tag={tag_slug}"

    all_interfaces = []

    while interface_url:
        response = requests.get(interface_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            interfaces = data["results"]
            for interface in interfaces:
                interface_id = interface["id"]
                interface_name = interface["name"]
                interface_last_updated = interface["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(interface_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    # tags = interface.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]
                    print(f"The interface {interface_name} has this ID {interface_id} and the last update was {interface_last_updated}")
                    all_interfaces.append((interface_id))
                
            interface_url = data["next"]
        else:
            print("Error while fetching interfaces from Netbox.")
            print(response.text)
            return None

    return all_interfaces

# Function to get all virtual machines with {tag}
def get_old_virtual_machines(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    vm_url = NETBOX_URL + f"api/virtualization/virtual-machines/?tag={tag_slug}"

    all_vms = []

    while vm_url:
        response = requests.get(vm_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            vms = data["results"]
            for vm in vms:
                vm_id = vm["id"]
                vm_name = vm["name"]
                vm_last_updated = vm["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(vm_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    # tags = vm.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]
                    print(f"The VM {vm_name} has this ID {vm_id} and the last update was {vm_last_updated}")
                    all_vms.append((vm_id))
                
            vm_url = data["next"]
        else:
            print("Error while fetching virtual machines from Netbox.")
            print(response.text)
            return None

    return all_vms

# Function to get all clusters with {tag}
def get_old_clusters(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    cluster_url = NETBOX_URL + f"api/virtualization/clusters/?tag={tag_slug}"

    all_clusters = []

    while cluster_url:
        response = requests.get(cluster_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            clusters = data["results"]
            for cluster in clusters:
                cluster_id = cluster["id"]
                cluster_name = cluster["name"]
                cluster_last_updated = cluster["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(cluster_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    # tags = cluster.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]
                    print(f"The cluster {cluster_name} has this ID {cluster_id} and the last update was {cluster_last_updated}")
                    all_clusters.append((cluster_id))
                
            cluster_url = data["next"]
        else:
            print("Error while fetching clusters from Netbox.")
            print(response.text)
            return None

    return all_clusters

# Function to get all cluster groups with {tag}
def get_old_cluster_groups(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    cluster_group_url = NETBOX_URL + f"api/virtualization/cluster-groups/?tag={tag_slug}"

    all_cluster_groups = []

    while cluster_group_url:
        response = requests.get(cluster_group_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            cluster_groups = data["results"]
            for cluster_group in cluster_groups:
                cluster_group_id = cluster_group["id"]
                cluster_group_name = cluster_group["name"]
                cluster_group_last_updated = cluster_group["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(cluster_group_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    tags = cluster_group.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]
                    print(f"The cluster group {cluster_group_name} has this ID {cluster_group_id} and the last update was {cluster_group_last_updated}")
                    all_cluster_groups.append((cluster_group_id))
                
            cluster_group_url = data["next"]
        else:
            print("Error while fetching cluster groups from Netbox.")
            print(response.text)
            return None

    return all_cluster_groups

# Function to get all ip addresses with {tag}
def get_old_ip_addresses(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    ip_address_url = NETBOX_URL + f"api/ipam/ip-addresses/?tag={tag_slug}"

    all_ip_addresses = []

    while ip_address_url:
        response = requests.get(ip_address_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            ip_addresses = data["results"]
            for ip_address in ip_addresses:
                ip_address_id = ip_address["id"]
                ip_address_address = ip_address["address"]
                ip_address_last_updated = ip_address["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(ip_address_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    # tags = ip_address.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]
                    print(f"The IP address {ip_address_address} has this ID {ip_address_id} and the last update was {ip_address_last_updated}")
                    all_ip_addresses.append((ip_address_id))
                
            ip_address_url = data["next"]
        else:
            print("Error while fetching IP addresses from Netbox.")
            print(response.text)
            return None

    return all_ip_addresses

# Function to get all platforms with {tag}
def get_old_platforms(tag_slug):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    platform_url = NETBOX_URL + f"api/dcim/platforms/?tag={tag_slug}"

    all_platforms = []  # Lista per memorizzare gli ID delle piattaforme obsolete

    while platform_url:
        response = requests.get(platform_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            platforms = data["results"]
            for platform in platforms:
                platform_id = platform["id"]
                platform_name = platform["name"]
                platform_last_updated = platform["last_updated"]
                
                # Convert last_updated to datetime object
                last_updated_date = datetime.strptime(platform_last_updated, '%Y-%m-%dT%H:%M:%S.%fZ')
                
                # Calculate the difference in days between today and last_updated
                days_difference = (datetime.utcnow() - last_updated_date).days
                
                if days_difference > days_rentention:
                    # tags = platform.get("tags", [])
                    # tag_ids = [str(tag["id"]) for tag in tags]
                    print(f"The platform {platform_name} has this ID {platform_id} and the last update was {platform_last_updated}")
                    all_platforms.append(platform_id)  # Aggiungi l'ID della piattaforma alla lista
                    
            platform_url = data["next"]
        else:
            print("Error while fetching platforms from Netbox.")
            print(response.text)
            return None
    
    return all_platforms  # Restituisci la lista degli ID delle piattaforme obsolete

# Function to get the IP info
def get_ips(address, vm_id, tag_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/ipam/ip-addresses/?address={address}", headers=headers, verify=False)
    if response.status_code == 200:
        ips_data = response.json()
        ips = ips_data["results"] 
        
        filtered_ips = []
        for ip in ips:
            if ip["assigned_object"] and \
               ip["assigned_object"]["virtual_machine"] and \
               ip["assigned_object"]["virtual_machine"]["id"] == vm_id and \
               any(tag["name"] == tag_name for tag in ip["tags"]):
                filtered_ips.append(ip)
        
        if not filtered_ips:
            print(f"No IP addresses found for address '{address}', VM ID '{vm_id}', and tag name '{tag_name}'.")
        
        return filtered_ips
    else:
        print(f"Error while fetching IP addresses from Netbox: {response.text}")
        return []

# Function to get the ID of the interface associated with a VM based on the MAC address of the interface
def get_interface_id_by_mac(vm_name, mac_address):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/virtualization/interfaces/?virtual_machine={vm_name}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        for interface in data["results"]:
            if interface["mac_address"].lower() == mac_address.lower():  # Case-insensitive comparison
                return interface["id"]
        print(f"Interface with MAC address '{mac_address}' not found on Netbox for virtual machine '{vm_name}'.")
        return None
    else:
        print(f"Error while searching for interface with MAC address '{mac_address}' for virtual machine '{vm_name}' on Netbox.")
        return None

# Function to get information about nic
def get_nics(vm_id,nic_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    params = {
        "virtual_machine_id": vm_id,
        "name": nic_name  # Aggiungi il filtro per il nome della NIC se specificato
    }
    response = requests.get(NETBOX_URL + f"api/virtualization/interfaces/?virtual_machine_id={vm_id}", params=params, headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"]
        else:
            if nic_name:
                print(f"No interface named '{nic_name}' found for virtual machine with ID '{vm_id}'.")
            else:
                print(f"No interfaces found for virtual machine with ID '{vm_id}'.")
            return None
    else:
        print(f"Error while searching for interfaces for virtual machine with ID '{vm_id}' on Netbox.")
        return None

# Function to get the ID of a virtual machine from Netbox
def get_vm_info(vm_name, tag_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/virtualization/virtual-machines/?name={vm_name}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            for vm in data["results"]:
                tag_info = vm['tags']
                tag_id_tocheck = tag_info[0]["id"]
                if tag_id_tocheck == tag_id:
                    return vm
        else:
            print(f"Virtual machine '{vm_name}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for virtual machine '{vm_name}' on Netbox.")
        print(response.text)
        return None

# Function to get the ID of host
def get_hosts_id(host_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/dcim/devices/?name={host_name}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Hosts '{host_name}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for device type '{host_name}' on Netbox.")
        print(response.text)
        return None

# Function to get the ID of a manufacturer from Netbox
def get_manufacturer_id(manufacturer, tag_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/dcim/manufacturers/?name={manufacturer}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Manufacturer '{manufacturer}' not found on Netbox. Creating...")
            new_manufacturer_data = {
                "name": manufacturer,
                "slug": manufacturer.replace(" ","").replace(".", ""),
                "tags": [tag_id]
                # Add other fields if necessary for manufacturer creation
            }
            response = requests.post(NETBOX_URL + "api/dcim/manufacturers/", headers=headers, json=new_manufacturer_data, verify=False)
            if response.status_code == 201:
                print(f"Manufacturer '{manufacturer}' created successfully on Netbox!")
                # Get the ID of the newly created manufacturer
                new_manufacturer_id = response.json()["id"]
                return new_manufacturer_id
            else:
                print(f"Error creating manufacturer '{manufacturer}' on Netbox.")
                print(response.text)
                return None
    else:
        print(f"Error while searching for manufacturer '{manufacturer}' on Netbox.")
        print(response.text)
        return None

# Function to get the ID of a device type from Netbox
def get_device_type_id(device_type):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/dcim/device-types/?model={device_type}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Device type '{device_type}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for device type '{device_type}' on Netbox.")
        print(response.text)
        return None


# Function to get existing cluster group by name
def get_clustergroups(name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    params = {
        "name": name
    }
    response = requests.get(NETBOX_URL + "api/virtualization/cluster-groups/", headers=headers, params=params, verify=False)
    if response.status_code == 200:
        cluster_groups = response.json()["results"]
        for cluster_group in cluster_groups:
            if cluster_group["name"] == name:
                return cluster_group
    return None

# Function to get the ID of a tenant from Netbox
def get_tenant_id(tenant):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/tenancy/tenants/?name={tenant}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Tenant '{tenant}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for tenant '{tenant}' on Netbox.")
        print(response.text)
        return None
    
# Function to get the ID of a site from Netbox
def get_site_id(site):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/dcim/sites/?name={site}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Site '{site}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for site '{site}' on Netbox.")
        print(response.text)
        return None
    
# Function to get the ID of a tag from Netbox
def get_tag_id(tag):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/extras/tags/?name={tag}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Tag '{tag}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for tag '{tag}' on Netbox.")
        print(response.text)
        return None
    
# Function to get the ID of a role from Netbox
def get_role_id(role):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/dcim/device-roles/?name={role}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Role '{role}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for role '{role}' on Netbox.")
        print(response.text)
        return None
    
def get_platform_id(platform, tag_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/dcim/platforms/?name={platform}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Platform '{platform}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for platform '{platform}' on Netbox.")
        print(response.text)
        return None
    
# Function to get the ID of a cluster from Netbox
def get_cluster_id(cluster):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/virtualization/clusters/?name={cluster}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"]
        else:
            print(f"Cluster '{cluster}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for cluster '{cluster}' on Netbox.")
        print(response.text)
        return None

# Function to get the ID of a cluster type from Netbox
def get_cluster_type_id(cluster_type):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/virtualization/cluster-types/?name={cluster_type}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Cluster type '{cluster_type}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for cluster type '{cluster_type}' on Netbox.")
        print(response.text)
        return None

# Function to get the ID of a cluster group from Netbox
def get_cluster_group_id(cluster_group):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(NETBOX_URL + f"api/virtualization/cluster-groups/?name={cluster_group}", headers=headers, verify=False)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]["id"]
        else:
            print(f"Cluster group '{cluster_group}' not found on Netbox.")
            return None
    else:
        print(f"Error while searching for cluster group '{cluster_group}' on Netbox.")
        print(response.text)
        return None
    
# Functions to create the Objects
    
# Function to create an IP address on Netbox
def create_ip_address(tenant_id, tag_id, interface_id,data):
    data["address"] = data['address']
    data["tenant"] = tenant_id
    data["tags"] = [tag_id]
    data["assigned_object_type"] = "virtualization.vminterface"
    data["assigned_object_id"] = interface_id

    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.post(NETBOX_URL + "api/ipam/ip-addresses/", json=data, headers=headers, verify=False)
    if response.status_code == 201:
        print(f"IP address '{data['address']}' created successfully on Netbox.")
    else:
        print(f"Error creating IP address '{data['address']}' on Netbox.")
        print(response.text)

# Function to create an IP address on Netbox
def update_ip_address(ip_id,tenant_id,tag_id,interface_id,data):
    data["address"] = data['address']
    data["tenant"] = tenant_id
    data["tags"] = [tag_id]
    data["assigned_object_type"] = "virtualization.vminterface"
    data["assigned_object_id"] = interface_id
    
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.patch(NETBOX_URL + f"api/ipam/ip-addresses/{ip_id}/", json=data, headers=headers, verify=False)
    if response.status_code == 200:
        print(f"IP address '{data['address']}' updated successfully on Netbox.")
    else:
        print(f"Error updating IP address '{data['address']}' on Netbox.")
        print(response.text)

# Function to create a Host on Netbox
def create_host(data):
    # Get IDs for role, tenant, manufacturer, device type, platform, site, cluster, and tags
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        tag_id = create_tag(data["tags"])
    role_id = get_role_id(data["role"])
    if role_id is None:
        role_id = create_role(data["role"])
    tenant_id = get_tenant_id(data["tenant"])
    if tenant_id is None:
        tenant_id = create_tenant(data["tenant"])
    manufacturer_id = get_manufacturer_id(data["manufacturer"], tag_id)
    device_type = get_device_type_id(data["device_type"])
    if device_type is None:
        device_type = create_device_type(data["device_type"],manufacturer_id)
    platform = get_platform_id(data["platform"], tag_id)
    if platform is None:
        platform = create_platform(data["platform"], tag_id)
    site_id = get_site_id(data["site"])
    if site_id is None:
        site_id = create_site(data["site"])
    cluster_info = get_cluster_id(data["cluster"])
    if cluster_info:
        cluster_id = cluster_info[0]['id']
    else:
        cluster_id = create_cluster(data["cluster"])
    
    if role_id is not None and tenant_id is not None and manufacturer_id is not None and device_type is not None and platform is not None and site_id is not None and cluster_id is not None and tag_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["role"] = role_id
        data["tenant"] = tenant_id
        data["manufacturer"] = manufacturer_id
        data["device_type"] = device_type
        data["platform"] = platform
        data["site"] = site_id
        data["cluster"] = cluster_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        
        # Add the custom field for memory
        custom_fields = {
            "vcsa_host_memory": data["vcsa_host_memory"]
        }
        data["custom_fields"] = custom_fields

        response = requests.post(NETBOX_URL + "api/dcim/devices/", headers=headers, json=data, verify=False)
        if response.status_code == 201:
            print(f"Host '{data['name']}' created successfully on Netbox!")
        else:
            print(f"Error creating Host '{data['name']}' on Netbox.")
            print(response.text)
    else:
        print("Unable to create the Host on Netbox due to missing information.")

# Function to update hosts information
def update_host(host_id,data):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    # Get IDs for role, tenant, manufacturer, device type, platform, site, cluster, and tags
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        tag_id = create_tag(data["tags"])
    role_id = get_role_id(data["role"])
    if role_id is None:
        role_id = create_role(data["role"])
    tenant_id = get_tenant_id(data["tenant"])
    if tenant_id is None:
        tenant_id = create_tenant(data["tenant"])
    manufacturer_id = get_manufacturer_id(data["manufacturer"], tag_id)
    device_type = get_device_type_id(data["device_type"])
    if device_type is None:
        device_type = create_device_type(data["device_type"],manufacturer_id)
    platform = get_platform_id(data["platform"], tag_id)
    if platform is None:
        platform = create_platform(data["platform"], tag_id)
    site_id = get_site_id(data["site"])
    if site_id is None:
        site_id = create_site(data["site"])
    cluster_info = get_cluster_id(data["cluster"])
    if cluster_info:
        cluster_id = cluster_info[0]['id']
    else:
        cluster_id = create_cluster(data["cluster"])
    
    if role_id is not None and tenant_id is not None and manufacturer_id is not None and device_type is not None and platform is not None and site_id is not None and cluster_id is not None and tag_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["role"] = role_id
        data["tenant"] = tenant_id
        data["manufacturer"] = manufacturer_id
        data["device_type"] = device_type
        data["platform"] = platform
        data["site"] = site_id
        data["cluster"] = cluster_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        
        # Add the custom field for memory
        custom_fields = {
            "vcsa_host_memory": data["vcsa_host_memory"]
        }
        data["custom_fields"] = custom_fields
        response = requests.patch(NETBOX_URL + f"api/dcim/devices/{host_id}/", headers=headers, json=data, verify=False)
        if response.status_code == 200:
            print(f"Host '{data['name']}' updated successfully on Netbox!")
        else:
            print(f"Error updating Host '{data['name']}' on Netbox.")
            print(response.text)
    else:
        print("Unable to update the Host on Netbox due to missing information.")

# Function to create a platform in Netbox
def create_platform(platform_name, tag_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_platform_data = {
        "name": platform_name,
        "slug": platform_name.replace(" ", "").replace(".", "").replace("/", ""),
        "tags": [tag_id]
        # Add other fields if necessary for platform creation
    }
    response = requests.post(NETBOX_URL + "api/dcim/platforms/", headers=headers, json=new_platform_data, verify=False)
    if response.status_code == 201:
        print(f"Platform '{platform_name}' successfully created on Netbox!")
        # Get the ID of the newly created platform
        new_platform_id = response.json()["id"]
        return new_platform_id
    else:
        print(f"Error while creating platform '{platform_name}' on Netbox.")
        print(response.text)
        return None

# Function to create the device type
def create_device_type(device_type, manufacturer_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_device_type_data = {
        "model": device_type,
        "manufacturer": manufacturer_id,
        "slug": device_type.lower().replace(" ", "-"),
        # Add other fields if necessary for device type creation
    }
    response = requests.post(NETBOX_URL + "api/dcim/device-types/", headers=headers, json=new_device_type_data, verify=False)
    if response.status_code == 201:
        print(f"Device type '{device_type}' successfully created on Netbox!")
        # Get the ID of the newly created device type
        new_device_type_id = response.json()["id"]
        return new_device_type_id
    else:
        print(f"Error while creating device type '{device_type}' on Netbox.")
        return None

# Function to create a tenant in Netbox
def create_tenant(tenant_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_tenant_data = {
        "name": tenant_name,
        # Add other fields if necessary for tenant creation
    }
    response = requests.post(NETBOX_URL + "api/tenancy/tenants/", headers=headers, json=new_tenant_data, verify=False)
    if response.status_code == 201:
        print(f"Tenant '{tenant_name}' successfully created on Netbox!")
        # Get the ID of the newly created tenant
        new_tenant_id = response.json()["id"]
        return new_tenant_id
    else:
        print(f"Error while creating tenant '{tenant_name}' on Netbox.")
        print(response.text)
        return None

# Function to create a site in Netbox
def create_site(site_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_site_data = {
        "name": site_name,
        # Add other fields if necessary for site creation
    }
    response = requests.post(NETBOX_URL + "api/dcim/sites/", headers=headers, json=new_site_data, verify=False)
    if response.status_code == 201:
        print(f"Site '{site_name}' successfully created on Netbox!")
        # Get the ID of the newly created site
        new_site_id = response.json()["id"]
        return new_site_id
    else:
        print(f"Error while creating site '{site_name}' on Netbox.")
        print(response.text)
        return None

# Function to create a tag in Netbox
def create_tag(tag_name, tag_slug, tag_description):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_tag_data = {
        "name": tag_name,
        "slug": tag_slug,
        "description": tag_description
        # Add other fields if necessary for tag creation
    }
    response = requests.post(NETBOX_URL + "api/extras/tags/", headers=headers, json=new_tag_data, verify=False)
    if response.status_code == 201:
        print(f"Tag '{tag_name}' successfully created on Netbox!")
        # Get the ID of the newly created tag
        new_tag_id = response.json()["id"]
        return new_tag_id
    else:
        print(f"Error while creating tag '{tag_name}' on Netbox.")
        print(response.text)
        return None

# Function to update tag in Netbox
def update_tag(tag_id, tag_name, tag_slug, tag_description):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_tag_data = {
        "name": tag_name,
        "slug": tag_slug,
        "description": tag_description
        # Add other fields if necessary for tag creation
    }
    response = requests.patch(NETBOX_URL + f"api/extras/tags/{tag_id}/", headers=headers, json=new_tag_data, verify=False)
    if response.status_code == 200:
        print(f"Tag with ID '{tag_id}' updated successfully on Netbox!")
        return True
    else:
        print(f"Error while updating tag with ID '{tag_id}' on Netbox.")
        print(response.text)
        return False

# Function to create a cluster type in oVirt
def create_cluster_type(cluster_type_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_cluster_type_data = {
        "name": cluster_type_name,
        # Add other fields if necessary for role creation
    }
    response = requests.post(NETBOX_URL + "api/clusters", headers=headers, data=new_cluster_type_data, verify=False)
    if response.status_code == 201:
        print(f"Cluster type '{cluster_type_name}' successfully created in oVirt!")
        # Get the ID of the newly created cluster type
        new_cluster_type_id = response.json()["id"]
        return new_cluster_type_id
    else:
        print(f"Error while creating cluster type '{cluster_type_name}' in oVirt.")
        print(response.text)
        return None

# Function to create a role in Netbox
def create_role(role_name):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    new_role_data = {
        "name": role_name,
        # Add other fields if necessary for role creation
    }
    response = requests.post(NETBOX_URL + "api/dcim/device-roles/", headers=headers, json=new_role_data, verify=False)
    if response.status_code == 201:
        print(f"Role '{role_name}' successfully created on Netbox!")
        # Get the ID of the newly created role
        new_role_id = response.json()["id"]
        return new_role_id
    else:
        print(f"Error while creating role '{role_name}' on Netbox.")
        print(response.text)
        return None
    
# Function to create Cluster Group on ovirt
def create_clustergroups(data):
    # Create the tag if it doesn't exist
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        print("Tag not found. Creating tag...")
        tag_id = create_tag(data["tags"], data["tags"].replace(" ", "").replace(":", "").lower(),tag_description)

    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    data["tags"] = [tag_id] 

    response = requests.post(NETBOX_URL + "api/virtualization/cluster-groups/", headers=headers, json=data, verify=False)
    if response.status_code == 201:
        print(f"Cluster Group '{data['name']}' created successfully on Netbox!")
    else:
        print(f"Error creating cluster group '{data['name']}' on Netbox.")
        print(response.text)

# Function to update Cluster Group on oVirt
def update_clustergroups(clustergroups_id,data):
    # Create the tag if it doesn't exist
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        print("Tag not found. Creating tag...")
        tag_id = create_tag(data["tags"], data["tags"].replace(" ", "").lower(),tag_description)
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    data["tags"] = [tag_id] 

    response = requests.patch(NETBOX_URL + f"api/virtualization/cluster-groups/{clustergroups_id}/", headers=headers, json=data, verify=False)
    if response.status_code == 200:
        print(f"Cluster group '{data['name']}' updated successfully on Netbox!")
        return True
    else:
        print(f"Error while updating cluster group '{data['name']}' on Netbox.")
        print(response.text)
        return False

# Function to create a Cluster on Netbox
def create_cluster(data):
    # Get IDs for cluster type, cluster group, tenant, and site
    cluster_type_id = get_cluster_type_id(data["type"])
    if cluster_type_id is None:
        cluster_type_id = create_cluster_type(data["type"])

    cluster_group_id = get_cluster_group_id(data["group"])

    # Create the tenant if it doesn't exist
    tenant_id = get_tenant_id(data["tenant"])
    if tenant_id is None:
        print("Tenant id not found. Creating ...")
        tenant_id = create_tenant(data["tenant"])
    
    # Create site if it doesn't exist 
    site_id = get_site_id(data["site"])
    if site_id is None:
        print ("Site id not found. Creating ...")
        site_id = create_site(data["site"])
    
    # Create the tag if it doesn't exist
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        print("Tag not found. Creating tag...")
        tag_id = create_tag(data["tags"], data["tags"].replace(" ", "").lower())

    if cluster_type_id is not None and cluster_group_id is not None and tenant_id is not None and site_id is not None and tag_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["type"] = cluster_type_id
        data["group"] = cluster_group_id
        data["tenant"] = tenant_id
        data["site"] = site_id
        data["tags"] = [tag_id]  # Put the tag ID in a list

        response = requests.post(NETBOX_URL + "api/virtualization/clusters/", headers=headers, json=data, verify=False)
        if response.status_code == 201:
            print(f"Cluster '{data['name']}' created successfully on Netbox!")
        else:
            print(f"Error creating cluster '{data['name']}' on Netbox.")
            print(response.text)
    else:
        print("Unable to create cluster on Netbox due to missing information.")

# Function to update a Cluster on Netbox
def update_cluster(cluster_id, data):

    # Get IDs for cluster type, cluster group, tenant, and site
    cluster_type_id = get_cluster_type_id(data["type"])
    if cluster_type_id is None:
        cluster_type_id = create_cluster_type(data["type"])

    cluster_group_id = get_cluster_group_id(data["group"])

    # Create the tenant if it doesn't exist
    tenant_id = get_tenant_id(data["tenant"])
    if tenant_id is None:
        print("Tenant id not found. Creating ...")
        tenant_id = create_tenant(data["tenant"])
    
    # Create site if it doesn't exist 
    site_id = get_site_id(data["site"])
    if site_id is None:
        print ("Site id not found. Creating ...")
        site_id = create_site(data["site"])
    
    # Create the tag if it doesn't exist
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        print("Tag not found. Creating tag...")
        tag_id = create_tag(data["tags"], data["tags"].replace(" ", "").lower())

    if cluster_type_id is not None and cluster_group_id is not None and tenant_id is not None and site_id is not None and tag_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }

        data["type"] = cluster_type_id
        data["group"] = cluster_group_id
        data["tenant"] = tenant_id
        data["site"] = site_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        
        response = requests.patch(NETBOX_URL + f"api/virtualization/clusters/{cluster_id}/", headers=headers, json=data, verify=False)
        if response.status_code == 200:
            print(f"Cluster '{data['name']}' updated successfully on Netbox!")
        else:
            print(f"Error updating cluster '{data['name']}' on Netbox.")
            print(response.text)
    else:
        print("Unable to update cluster on Netbox due to missing information.")

# Function to create a VM on Netbox
def create_vm(data):
    # Get IDs
    tenant_id = get_tenant_id(data["tenant"])
    if tenant_id is None:
        tenant_id = create_tenant(data["tenant"])
    site_id = get_site_id(data["site"])
    if site_id is None:
        site_id = create_site(data["site"])
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        tag_id = create_tag(data["tags"])
    role_id = get_role_id(data["role"])
    if role_id is None:
        role_id = create_role(data["role"])
    cluster_info = get_cluster_id(data["cluster"])
    if cluster_info:
        cluster_id = cluster_info[0]['id']
    else:
        cluster_id = create_cluster(data["cluster"])

    # Check if the "platform" field in the CSV file is empty
    if data["platform"].strip():
        platform_id = get_platform_id(data["platform"], tag_id)
        if platform_id is None:
            platform_id = create_platform(data["platform"], tag_id)
    else:
        platform_id = None

    if tenant_id is not None and site_id is not None and tag_id is not None and role_id is not None and cluster_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["tenant"] = tenant_id
        data["site"] = site_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        data["role"] = role_id
        data["cluster"] = cluster_id
        if platform_id is not None:
            data["platform"] = platform_id
        else:
            del data["platform"]  # Remove the "platform" field from the payload if it's empty

        # Check if the "device" field is empty before including it in the request payload
        if data["device"]:
            response = requests.post(NETBOX_URL + "api/virtualization/virtual-machines/", headers=headers, json=data, verify=False)
        else:
            del data["device"]  # Remove the "device" field from the request payload

        response = requests.post(NETBOX_URL + "api/virtualization/virtual-machines/", headers=headers, json=data, verify=False)
        if response.status_code == 201:
            print(f"VM '{data['name']}' created successfully on Netbox!")
        else:
            print(f"Error creating VM '{data['name']}' on Netbox.")
            print(response.text)
    else:
        print("Unable to create the VM on Netbox due to missing information.")

# Function to udpate a VM on Netbox
def update_vm(vm_id,data):
    # Get IDs
    tenant_id = get_tenant_id(data["tenant"])
    if tenant_id is None:
        tenant_id = create_tenant(data["tenant"])
    site_id = get_site_id(data["site"])
    if site_id is None:
        site_id = create_site(data["site"])
    tag_id = get_tag_id(data["tags"])
    if tag_id is None:
        tag_id = create_tag(data["tags"])
    role_id = get_role_id(data["role"])
    if role_id is None:
        role_id = create_role(data["role"])
    cluster_info = get_cluster_id(data["cluster"])
    if cluster_info:
        cluster_id = cluster_info[0]['id']
    else:
        cluster_id = create_cluster(data["cluster"])

    # Check if the "platform" field in the CSV file is empty
    if data["platform"].strip():
        platform_id = get_platform_id(data["platform"], tag_id)
        if platform_id is None:
            platform_id = create_platform(data["platform"], tag_id)
    else:
        platform_id = None

    if tenant_id is not None and site_id is not None and tag_id is not None and role_id is not None and cluster_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["tenant"] = tenant_id
        data["site"] = site_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        data["role"] = role_id
        data["cluster"] = cluster_id
        if platform_id is not None:
            data["platform"] = platform_id
        else:
            del data["platform"]  # Remove the "platform" field from the payload if it's empty

        # Check if the "device" field is empty before including it in the request payload
        if data["device"]:
            response = requests.patch(NETBOX_URL + f"api/virtualization/virtual-machines/{vm_id}/", headers=headers, json=data, verify=False)
        else:
            del data["device"]  # Remove the "device" field from the request payload

        response = requests.patch(NETBOX_URL + f"api/virtualization/virtual-machines/{vm_id}/", headers=headers, json=data, verify=False)
        if response.status_code == 200:
            print(f"VM '{data['name']}' updated successfully on Netbox!")
        else:
            print(f"Error updating VM '{data['name']}' on Netbox.")
            print(response.text)
    else:
        print("Unable to update the VM on Netbox due to missing information.")

# Function to create an interface on Netbox
def create_interface(vm_id,data):
    # Get the ID of the tenant, site, and tag
    tenant_id = get_tenant_id(data["tenant"])
    tag_id = get_tag_id(data["tags"])
    
    # Check if the fields are valid
    if tenant_id is not None and tag_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["tenant"] = tenant_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        data["virtual_machine"] = vm_id
        
        # Make the POST request to create the interface
        response = requests.post(NETBOX_URL + "api/virtualization/interfaces/", headers=headers, json=data, verify=False)
        if response.status_code == 201:
            print(f"Interface '{data['name']}' created successfully for VM '{data['virtual_machine']}' on Netbox!")
        else:
            print(f"Error while creating interface '{data['name']}' on Netbox for VM '{data['virtual_machine']}'.")
            print(response.text)
    else:
        print("Unable to create the interface on Netbox due to missing information.")


def update_interface(nic_info,vm_id,data):
    # Get the ID of the tenant, site, and tag
    tenant_id = get_tenant_id(data["tenant"])
    tag_id = get_tag_id(data["tags"])
    
    # Check if the fields are valid
    if tenant_id is not None and tag_id is not None:
        headers = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        data["tenant"] = tenant_id
        data["tags"] = [tag_id]  # Put the tag ID in a list
        data["virtual_machine"] = vm_id
        nic_id = nic_info[0]["id"]
        # Make the POST request to create the interface
        response = requests.patch(NETBOX_URL + f"api/virtualization/interfaces/{nic_id}/", headers=headers, json=data, verify=False)
        if response.status_code == 200:
            print(f"Interface '{data['name']}' updated successfully for VM '{data['virtual_machine']}' on Netbox!")
        else:
            print(f"Error while updating interface '{data['name']}' on Netbox for VM '{data['virtual_machine']}'.")
            print(response.text)
    else:
        print("Unable to updated the interface on Netbox due to missing information.")


# Functions to delete objects
        
# Function to delete devices
def delete_devices(devices_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/dcim/devices/{devices_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"Device with ID {devices_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete device with ID {devices_id}.")
        print(f"Response: {response.text}")
        return False

# Function to delete interface
def delete_interfaces(interfaces_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/virtualization/interfaces/{interfaces_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"Interface with ID {interfaces_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete Interface with ID {interfaces_id}.")
        print(f"Response: {response.text}")
        return False

# Function to delete virtual machine
def delete_virtual_machines(virtual_machines_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/virtualization/virtual-machines/{virtual_machines_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"Virtual Machine with ID {virtual_machines_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete Virtual Machine with ID {virtual_machines_id}.")
        print(f"Response: {response.text}")
        return False

# Function to delete cluster
def delete_clusters(clusters_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/virtualization/clusters/{clusters_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"Cluster with ID {clusters_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete Cluster with ID {clusters_id}.")
        print(f"Response: {response.text}")
        return False

# Function to delete cluster groups
def delete_cluster_groups(cluster_groups_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/virtualization/cluster-groups/{cluster_groups_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"Cluster Group with ID {cluster_groups_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete Cluster Group with ID {cluster_groups_id}.")
        print(f"Response: {response.text}")
        return False

# Function to delete ip address
def delete_ip_addresses(ip_addresses_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/ipam/ip-addresses/{ip_addresses_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"IP Address with ID {ip_addresses_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete IP Address with ID {ip_addresses_id}.")
        print(f"Response: {response.text}")
        return False
    
# Function to delete platform
def delete_platforms(platforms_id):
    headers = {
        "Authorization": f"Token {NETBOX_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.delete(NETBOX_URL + f"api/dcim/platforms/{platforms_id}", headers=headers, verify=False)
    if response.status_code == 204:
        print(f"Platform with ID {platforms_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete Platform with ID {platforms_id}.")
        print(f"Response: {response.text}")
        return False