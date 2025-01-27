# oVirt - Netbox Sync


## Getting started

This project provides a set of scripts to synchronize data from an oVirt/RHV environment to NetBox, leveraging NetBox as the source of truth for your infrastructure. It extracts information about Data Centers, Clusters, Hosts, and Virtual Machines (VMs), including their associated network interfaces and IP addresses.

## Overview

The synchronization process involves the following steps:

1. Data Extraction: ```get-vminfo-ovirt.py``` retrieves data from the oVirt/RHV environment using the oVirt SDK (ovirtsdk4). It gathers details about:
    - [ ] Data Centers
    - [ ] Clusters
    - [ ] Hosts (including hardware information and network interfaces)
    - [ ] Virtual Machines (including disks, network interfaces, and guest agent reported IPs, if available)
2. Data Transformation: The extracted data is formatted and stored in CSV files within the ```exported_info directory```.
3. Data Loading: ```ovirt-sync.py``` orchestrates the execution of a series of scripts (located in the modules directory - not provided in your example, but inferred from the script's logic) that are responsible for importing the data from the CSV files into NetBox.
4. Object Deletion: ```delete-old-object.py``` delete old object in Netbox based on days_rentention variable.

## Scripts Description

- [ ] ```ovirt-sync.py```: This is the main script that controls the synchronization process. It executes a predefined sequence of scripts located in the modules directory. These modules (not provided in your example) are assumed to handle the actual import of data into NetBox, likely using the pynetbox library.
- [ ] ```config.py```: This script contains configuration settings for both oVirt/RHV and NetBox, including:
    - [ ] NetBox URL and API token (NETBOX_URL, NETBOX_TOKEN)
    - [ ] oVirt/RHV FQDN (host_fqdn)
    - [ ] Default values for site, tenant, tag, and VM role (site, tenant, tag, vm_role).
    - [ ] Retention time in days for old object deletion (days_rentention)
    - [ ] Various functions for interacting with the NetBox API, including:
      - [ ] Retrieving IDs of existing objects (data centers, clusters, hosts, VMs, etc.).
      - [ ] Creating objects in NetBox if they don't exist.
      - [ ] Updating objects in Netbox.
      - [ ] Deleting objects in Netbox.
- [ ] ```get-vminfo-ovirt.py```: This script connects to the oVirt/RHV environment, extracts data, and saves it to CSV files:
    - [ ] data_centers.csv
    - [ ] clusters.csv
    - [ ] hosts_info.csv
    - [ ] vms.csv
    - [ ] nics_vms.csv
    - [ ] ip_info.csv
- [ ] ```delete-old-object.py```: This script, which uses the functions defined in config.py, is used to delete the objects not updated in the last days_rentention days, using {tag} as a filter.

## Prerequisites

- [ ] ```oVirt Environment```: A running oVirt/RHV environment (version 4.x) with administrative access.
- [ ] ```NetBox Instance```: A running NetBox instance with an API token that has write permissions.
- [ ] ```Python 3```: Python 3.6 or higher is recommended.
- [ ] ```Required Python Libraries```:
  - [ ] ```ovirtsdk4```
  - [ ] ```requests```
  - [ ] ```pynetbox``` 
  - [ ] ```urllib3```
  - [ ] ```datetime```
      
Install the required libraries using pip:

      pip install ovirtsdk4 requests pynetbox urllib3

## Configuration

1. oVirt Credentials:
  - [ ] Modify the ```config.py``` file and update the following variables with your oVirt/RHV environment details:
    - [ ] ```host_fqdn``` The fully qualified domain name of your oVirt engine.
    - [ ] Change the ```password``` in the ```get-vminfo-ovirt.py``` script to the password of your oVirt administrative user, also modify the path to the ovirt certificate ```ca_file```.
    - [ ] ```site```, ```tenant```, ```tag```, ```vm_role```: Customize these variables with appropriate default values for your environment.
    - [ ] ```NETBOX_URL```: The URL of your NetBox instance.
    - [ ] ```NETBOX_TOKEN```: A valid API token for your NetBox instance.
2. NetBox API Token:
  - [ ] Create an API token in NetBox with read and write permissions.
  - [ ] Update the ```NETBOX_TOKEN``` variable in ```config.py``` with your NetBox API token.

## Usage

1. Run the main script:

           python ovirt-sync.py

This script will execute the other scripts in the following sequence: ```get-vminfo-ovirt.py```, followed by the scripts listed in the ```scripts``` variable inside ```ovirt-sync.py```. This script will delete the old objects not updated for ```days_rentention``` days.


## Important Notes:

- [ ] The ```modules``` directory is referenced in ```ovirt-sync.py``` but was not included in your provided code. You'll need to create this directory and add the necessary scripts for importing data into NetBox. These scripts are likely to utilize the functions defined in ```config.py``` to interact with the NetBox API.
- [ ] The first time you run the synchronization, it will populate NetBox with data from your oVirt/RHV environment. Subsequent runs will update existing objects in NetBox and create new ones as needed.
- [ ] Carefully review the ```config.py``` file and ensure that all settings are correctly configured for your environment.
- [ ] It is highly recommended to test this synchronization process in a non-production environment first.
- [ ] Security: Be mindful of storing sensitive information like passwords and API tokens. Consider using environment variables or a more secure method for managing credentials.
- [ ] Error Handling: The provided scripts have basic error handling, but you might want to enhance it for production use.

## Contributing:

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
