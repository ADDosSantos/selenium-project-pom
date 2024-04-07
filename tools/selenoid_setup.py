import os
import subprocess
import requests

# URL of the cm_windows_386.exe file
url = "https://github.com/aerokube/cm/releases/download/1.8.7/cm_windows_386.exe"

# Path to save the downloaded file
download_path = "cm.exe"

if not os.path.exists(download_path):
# Download the file
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, "wb") as f:
            f.write(response.content)
        print("Downloaded cm.exe successfully")
    else:
        print("Failed to download cm.exe")

# Start Selenoid and Selenoid-Ui
print("Start Selenoid and Selenoid-Ui...")
subprocess.run(["cm.exe", "selenoid", "start", "--vnc", "--browsers-json", "tools\\config\\browsers.json"])
subprocess.run(["cm.exe", "selenoid-ui", "start"])

# Validating status
print("... Status of Selenoid and Selenoid-Ui.")
subprocess.run(["cm.exe", "selenoid", "status"])
subprocess.run(["cm.exe", "selenoid-ui", "status"])