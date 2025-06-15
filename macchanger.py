# Run on linux systems to change the MAC address of a network interface
# Ensure you have macchanger installed: sudo apt install macchanger

import subprocess

subprocess.run(["macchanger", "-m", "00:11:22:33:44:55", "eth0"])
# This script changes the MAC address of the network interface eth0 to 00:11:22:33:44:55