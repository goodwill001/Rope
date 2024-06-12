import subprocess

# Run pip freeze to generate a list of installed packages
pip_freeze_output = subprocess.check_output(["pip freeze > dump.txt "])
print("dump.txt created successfully!")

# Use pip uninstall to remove all packages listed in dump.txt
pip_uninstall_output = subprocess.check_output(["pip uninstall -r dump.txt -y"])
print("Package uninstallation successful!")
