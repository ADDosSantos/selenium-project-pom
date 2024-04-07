import subprocess

# Stop Selenoid and Selenoid-UI
subprocess.run(["cm.exe", "selenoid", "stop"])
subprocess.run(["cm.exe", "selenoid-ui", "stop"])

# Clean up Selenoid and Selenoid-UI
subprocess.run(["cm.exe", "selenoid", "cleanup"])
subprocess.run(["cm.exe", "selenoid-ui", "cleanup"])

# Remove cm.exe (assuming it's in the current directory)
import os
os.remove("cm.exe")