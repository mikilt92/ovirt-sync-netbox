import ovirtsdk4 as sdk
import ovirtsdk4.types as types
import csv 
import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import config

# Create a connection to the server:
connection = sdk.Connection(
  url=f'https://{config.host_fqdn}/ovirt-engine/api',
  username="admin@ovirt@internalsso",
  password="AdminPassword",
  ca_file="PATH/ovirt.crt",
)

output_directory = "exported_info"

# Create directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get DataCenters info
data_centers_service = connection.system_service().data_centers_service()
data_centers = data_centers_service.list()

csv_file_path = os.path.join(output_directory, 'data_centers.csv')

# Open CSV file to write it
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['name', 'slug', 'tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Loop on DataCenter object and write on CSV File
    for data_center in data_centers:
        data_center_name = data_center.name
        slug = data_center_name.replace(" ", "").lower()

        # Write DataCenter information to CSV
        data_dict = {
            'name': data_center_name,
            'slug': slug,
            'tags': config.tag
        }
        writer.writerow(data_dict)

# Get Clusters Information
clusters_service = connection.system_service().clusters_service()
clusters = clusters_service.list()

csv_file_path = os.path.join(output_directory, 'clusters.csv')

# Open CSV file to write it
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['name', 'type', 'group', 'status', 'site', 'tenant', 'tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    datacenters_service = connection.system_service().data_centers_service()
    
    # Loop on Cluster object and write on CSV File
    for cluster in clusters:
        cluster_name = cluster.name
        cluster_id = cluster.id
        datacenter_id = cluster.data_center.id

        # Get DataCenter list
        datacenters = datacenters_service.list()
        for datacenter in datacenters:
            if datacenter.id == datacenter_id:
                datacenter_name = datacenter.name
                break
        
        # Write Cluster information  to CSV
        data_dict = {
            'name': cluster_name,
            'type' : config.type,
            'group' : datacenter_name,
            'status' : 'active',
            'site' : config.site,
            'tenant' : config.tenant,
            'tags' : config.tag
        }
        writer.writerow(data_dict)

# Get Host Information
host_service = connection.system_service().hosts_service()
hosts = host_service.list()

csv_file_path = os.path.join(output_directory, 'hosts_info.csv')

# Open CSV file to write Hosts info
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = [ 
        'name', 'role', 'tenant', 'manufacturer', 'device_type',
        'platform', 'serial', 'asset_tag','status', 'site',
        'location', 'rack', 'position', 'face', 'latitude', 'longitude', 'parent',
        'device_bay', 'airflow', 'virtual_chassis', 'vc_position', 'vc_priority', 
        'cluster','description', 'config_template', 'comments', 'tags', 'id', 'cf_vcsa_host_cpu_cores','cf_vcsa_host_memory'
    ]
 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
 
    for host in hosts:
        HostName = host.name
        HostMemory = host.memory / 1024 ** 3
        ip_addresses = []  # Initialize the ip_addresses list for each host
        # Retrieve detailed host information
        host_detail = host_service.host_service(host.id).get()
        host_model = host_detail.hardware_information.product_name
        host_manufacturer = host_detail.hardware_information.manufacturer
        host_serial = host_detail.hardware_information.serial_number
        host_os_version = host_detail.os.version.full_version

        # Retrieve the Datacenter and Cluster
        cluster = connection.follow_link(host.cluster)
        datacenter = connection.follow_link(cluster.data_center)
        ClusterName = cluster.name
        DatacenterName = datacenter.name

        # Retrieve network interfaces information
        nics_service = host_service.host_service(host.id).nics_service()
        nics = nics_service.list()
        ip_count = 1
        for nic in nics:
            if nic.ip is not None:
                if isinstance(nic.ip, list):  # Check if nic.ip is a list
                    for ip in nic.ip:
                        ip_addresses.append(f"IP{ip_count}:{ip.address}")
                        ip_count += 1
                else:  # If nic.ip is not a list, it's a single IP object
                    ip_addresses.append(f"IP{ip_count}:{nic.ip.address}")
                    ip_count += 1

        # Write host information including IP addresses to CSV
        data_dict = {
            'name': HostName,
            'role': 'Server',
            'tenant': config.tenant,
            'manufacturer': host_manufacturer,
            'device_type': host_model,
            'platform': host_os_version,
            'serial': host_serial,
            'asset_tag': '',
            'status': 'active',
            'site': config.site,
            'location': '',
            'rack': '' ,
            'position': '',
            'face': '',
            'latitude': '',
            'longitude': '',
            'parent': '',
            'device_bay': '',
            'airflow': '',
            'virtual_chassis': '',
            'vc_position': '',
            'vc_priority': '',
            'cluster': ClusterName,
            'description': '',
            'config_template': '',
            'comments': '',
            'tags': config.tag,
            'id': '',
            'cf_vcsa_host_cpu_cores': '',
            'cf_vcsa_host_memory': HostMemory,
        }
        writer.writerow(data_dict)
  
# Get VM Info
vms_service = connection.system_service().vms_service()
vms = vms_service.list()

csv_file_path = os.path.join(output_directory, 'vms.csv')

# Open CSV file to write VMs info
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = [
        'name', 'status', 'role', 'site', 'cluster', 'device', 
        'tenant', 'platform', 'vcpus', 'memory', 'disk', 
        'description', 'config_template', 'comments', 'tags', 'id'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    csv_file_path = os.path.join(output_directory, 'nics_vms.csv')

    # Open CSV file to write VM NICs info
    with open(csv_file_path, 'w', newline='') as nics_csvfile:
        nic_fieldnames = [
            'virtual_machine', 'name', 'parent', 'bridge', 'enabled', 'mac_address', 
            'mtu', 'description', 'mode', 'tenant', 'vrf', 'tags', 'id'
        ]
        nic_writer = csv.DictWriter(nics_csvfile, fieldnames=nic_fieldnames)
        nic_writer.writeheader()

        # Loop through each VM
        for vm in vms:
            vm_name = vm.name
            memory_gb = int(vm.memory / 1024 / 1024)  # Converti la memoria in GB e arrotonda verso il basso
            vm_status = 'active' if vm.status == types.VmStatus.UP else 'offline'

            if vm_status == 'active':
                # Get Operating System info solo se lo stato del server è up
                guest_operating_system = vm.guest_operating_system
                os_distribution = guest_operating_system.distribution if guest_operating_system else ""
                os_version = f"{guest_operating_system.version.major}" if guest_operating_system and guest_operating_system.version else ""
            else:
                os_distribution = ''
                os_version = ''

            # Get VM Disks info
            disk_attachments_service = vms_service.vm_service(vm.id).disk_attachments_service()
            disk_attachments = disk_attachments_service.list()

            total_disk_size_gb = 0  # Inizializza la variabile per la somma dei GB
            for disk_attachment in disk_attachments:
                disk = disk_attachment.disk
                disk_service = connection.system_service().disks_service().disk_service(disk.id)
                disk_info = disk_service.get()
                total_disk_size_gb += int(disk_info.provisioned_size / 1024 / 1024 / 1024)

            # Get cluster info
            cluster = connection.follow_link(vm.cluster)
            cluster_name = cluster.name

            # Write VMs info to CSV
            data_dict = {
                'name': vm_name, 
                'status': vm_status, 
                'role': 'Server', 
                'site': config.site, 
                'cluster': cluster_name, 
                'device': '', 
                'tenant': config.tenant, 
                'platform': f'{os_distribution} {os_version}', 
                'vcpus': vm.cpu.topology.cores * vm.cpu.topology.sockets, 
                'memory': memory_gb, 
                'disk': total_disk_size_gb, 
                'description': vm.comment, 
                'config_template': '', 
                'comments': '', 
                'tags': config.tag, 
                'id': ''
            }
            writer.writerow(data_dict)

            # Get NICs info for the VM
            nics_service = vms_service.vm_service(vm.id).nics_service()
            nics = nics_service.list()

            # Write NICs info to CSV
            for nic in nics:
                # Convert enabled info into lower format
                enabled_lower = str(nic.plugged).lower()
                
                nic_dict = {
                    'virtual_machine': vm_name,
                    'name': nic.name,
                    'parent': nic.vnic_profile.name if nic.vnic_profile else '',
                    'bridge': nic.network.name if nic.network else '',
                    'enabled': enabled_lower,
                    'mac_address': nic.mac.address if nic.mac else '',
                    'mtu': '',
                    'description': nic.description,
                    'mode': '',
                    'tenant': config.tenant,
                    'vrf': '',
                    'tags': config.tag,
                    'id': nic.id
                }
                nic_writer.writerow(nic_dict)

# Write information on ip_info.csv
csv_file_path = os.path.join(output_directory, 'ip_info.csv')

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = [
        'address', 'mac_address', 'vrf', 'tenant', 'status', 'role', 'device', 'virtual_machine', 'interface', 
        'is_primary', 'dns_name', 'description', 'comments', 'tags', 'id'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through all VMs
    for vm in vms:
        vm_name = vm.name

        vm_status = 'active' if vm.status == types.VmStatus.UP else 'offline'

        # Get VM's devices information
        reported_devices_service = vms_service.vm_service(vm.id).reported_devices_service()
        reported_devices = reported_devices_service.list()

        # Get information about VM's nics
        nics_service = vms_service.vm_service(vm.id).nics_service()
        nics = nics_service.list()

        # Create empty dictionary to store information 
        device_ips = {}

        for device in reported_devices:
            if device.vm.id == vm.id and vm.status == types.VmStatus.UP:
                if device.ips is not None:
                    for ip in device.ips:
                        if ':' not in ip.address:
                            if device.name not in device_ips:
                                device_ips[device.name] = {'ips': [], 'mac': ''}
                            device_ips[device.name]['ips'].append(ip.address)
                            if device.mac is not None:
                                device_ips[device.name]['mac'] = device.mac.address

        for device_name, device_info in device_ips.items():
            ip_vm_cleaned = ', '.join(device_info['ips'])

            ip_dict = {
                'address': ip_vm_cleaned,
                'mac_address': device_info['mac'],
                'vrf': '',
                'tenant': config.tenant,
                'status': 'active',
                'role': '',
                'device': device_name,
                'virtual_machine': vm_name,
                'interface': device_name,
                'is_primary': '',
                'dns_name': '',
                'description': '',
                'comments': '',
                'tags': config.tag,
                'id': '',
            }
            writer.writerow(ip_dict)

# Close the connection
connection.close()
