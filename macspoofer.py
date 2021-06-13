import subprocess

# Name of interface
interface = input("network interface > ")

# Set a new MAC address
new_mac_address = input("new MAC address >")

print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

# Run 'ifconfig wlan0 down' command in shell to deactivate a network interface named wlan0
subprocess.call("ifconfig " + interface + " down", shell=True)

# Changing MAC address
subprocess.call("ifconfig " + interface + " hw ether " + new_mac_address, shell=True)

# Activate wlan0 network interface
subprocess.call("ifconfig " + interface + " up", shell=True)
