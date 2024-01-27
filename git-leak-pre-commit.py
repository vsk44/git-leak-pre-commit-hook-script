#!/usr/bin/env python3
"""Helper script to be used as a pre-commit hook."""
import os
import sys
import subprocess
import tarfile
import zipfile
import requests

def gitleaksEnabled():
    """Determine if the pre-commit hook for gitleaks is enabled."""
    out = subprocess.getoutput("git config --bool hooks.gitleaks")
    if out == "false":
        return False
    return True

def gitleaksInstalled():
    """Determine if gitleaks is installed."""
    try:
        subprocess.run(["gitleaks"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except Exception as e:
        print(f"Error checking gitleaks installation: {e}")
        return False

def install_gitleaks():
    """Install gitleaks."""
    if sys.platform == "linux":
        try:
            download_url = "https://github.com/gitleaks/gitleaks/releases/download/v8.18.1/gitleaks_8.18.1_linux_x64.tar.gz"
            subprocess.run(["wget", download_url], check=True)
            
            # Extract gitleaks binary from the tar.gz archive
            with tarfile.open("gitleaks_8.18.1_linux_x64.tar.gz", "r:gz") as tar:
                tar.extract("gitleaks", path=".")
            
            subprocess.run(["sudo", "mv", "gitleaks", "/usr/local/bin/"], check=True)
            
            # Remove the downloaded archive
            os.remove("gitleaks_8.18.1_linux_x64.tar.gz")
        except subprocess.CalledProcessError as e:
            print(f"Error installing gitleaks: {e}")
            sys.exit(1)
    elif sys.platform == "darwin":
        subprocess.run(["brew", "install", "gitleaks"], check=True)
    elif sys.platform == "win32":
        # Download gitleaks zip file
        download_url = "https://github.com/gitleaks/gitleaks/releases/download/v8.18.1/gitleaks_8.18.1_windows_x64.zip"
        gitleaks_zip = "gitleaks.zip"
        response = requests.get(download_url, stream=True)
        with open(gitleaks_zip, "wb") as zip_file:
            for chunk in response.iter_content(chunk_size=128):
                zip_file.write(chunk)
        
        # Extract gitleaks.exe from the zip archive
        with zipfile.ZipFile(gitleaks_zip, 'r') as zip_ref:
            zip_ref.extract("gitleaks.exe", ".")
        
        # Remove the downloaded archive
        os.remove(gitleaks_zip)

    run_gitleaks()

def run_gitleaks():
    if gitleaksInstalled():
        if sys.platform == "win32":
            exitCode = os.system('gitleaks.exe protect -v --staged')
        elif sys.platform == "linux" or sys.platform == "darwin":
            exitCode = os.WEXITSTATUS(os.system('gitleaks protect -v --staged'))
        else:
            print("Non-supportive system.")
            sys.exit(1)

        if exitCode == 1:
            print('''Warning: gitleaks has detected sensitive information in your changes.
To disable the gitleaks precommit hook run the following command:

    git config hooks.gitleaks false
''')
            sys.exit(1)
    else:
        print("Gitleaks is not installed. Installing...")
        install_gitleaks()

if gitleaksEnabled():
    run_gitleaks()
else:
    print('gitleaks precommit disabled\
     (enable with `git config hooks.gitleaks true`)')
