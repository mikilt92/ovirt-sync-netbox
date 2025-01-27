import subprocess
import os
import urllib3

# Modules directory
modules_dir = "modules"

# List of scripts to execute in order
scripts = [
    "get-vminfo-ovirt.py",
    "import-data_centers.py",
    "import-clusters.py",
    "import-hosts_info.py",
    "import-vms.py",
    "import-nics_vms.py",
    "import-ip_info.py",
    "delete-old-object.py"
]

# Full paths of the scripts
scripts_paths = [os.path.join(modules_dir, script) for script in scripts]

# Loop through the list of scripts and execute them one by one
for script_path in scripts_paths:
    subprocess.run(["python", script_path])
