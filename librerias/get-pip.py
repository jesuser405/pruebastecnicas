# get-pip.py
import os
import tempfile
import urllib.request
import runpy

url = "https://bootstrap.pypa.io/get-pip.py"

with urllib.request.urlopen(url) as response:
    script = response.read()

tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
tmp.write(script)
tmp.close()

runpy.run_path(tmp.name, run_name="__main__")
os.unlink(tmp.name)
# Clean up the temporary file
# os.remove(tmp.name)  # Uncomment if you want to remove the file after execution
# Note: The script will install pip in the current Python environment.
# Ensure you have the necessary permissions to install packages.
# You can run this script using Python to install pip if it's not already installed.
# Usage: python get-pip.py
# This script downloads the get-pip.py script from the official source and executes it to install pip.
# Make sure you have an internet connection when running this script.
# This script is useful for setting up pip in environments where it is not already installed.
# It is a one-time setup script to ensure pip is available for package management.