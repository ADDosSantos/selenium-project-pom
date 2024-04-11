import subprocess

print("\n# Stopping Selenoid and Selenoid-UI, and removing containers")

try:
    subprocess.run(["cm.exe", "selenoid", "stop"])
    subprocess.run(["cm.exe", "selenoid-ui", "stop"])

    # Clean up Selenoid and Selenoid-UI
    subprocess.run(["cm.exe", "selenoid", "cleanup"])
    subprocess.run(["cm.exe", "selenoid-ui", "cleanup"])

    print("\n# Remove cm.exe (assuming it's in the current directory)\n")
    import os
    os.remove("cm.exe")

except FileNotFoundError as e:
    print(f"\nError: {e}. Is 'cm.exe' is installed and accessible?\n")


