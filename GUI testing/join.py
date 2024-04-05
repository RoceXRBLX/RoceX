import subprocess
import os
import time
import shutil
import webbrowser

file_path = os.path.expanduser("~/AppData/Local/Bloxstrap/Modifications/ClientSettings/ClientAppSettings.json")

# Check if the ClientAppSettings.json file exists
if not os.path.exists(file_path):
    # Run the Bloxstrap installer
    subprocess.run(r".\CodeStuff/bloxstrapinstall.exe")

# Wait for the file to exist
while not os.path.exists(file_path):
    print("File does not exist yet. Waiting...")
    time.sleep(1)

# Copy the local file to the correct directory
local_file_path = os.path.join(os.getcwd(), "CodeStuff/ClientAppSettings.json")
if os.path.exists(local_file_path):
    shutil.copy(local_file_path, file_path)
    print(f"File '{local_file_path}' copied to '{file_path}'.")
else:
    print(f"Local file '{local_file_path}' does not exist.")

# Open the Roblox place using the roblox:// URL scheme
url = "roblox://placeid=7390193918"
webbrowser.open(url)

# Run the udp-reverse-proxy executable
udp_reverse_proxy_path = os.path.join(os.getcwd(), "CodeStuff/udp-reverse-proxy.exe")
if os.path.exists(udp_reverse_proxy_path):
    args = [udp_reverse_proxy_path, "localhost:53640", "147.185.221.16:4033"]
    subprocess.run(args, shell=True)
else:
    print(f"Executable '{udp_reverse_proxy_path}' does not exist.")