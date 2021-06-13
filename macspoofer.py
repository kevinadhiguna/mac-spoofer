import subprocess

# Name of interface
interface = "wlan0"

# Run 'ifconfig wlan0 down' command in shell to deactivate a network interface named wlan0
subprocess.call("ifconfig wlan0 down", shell=True)

# Changing MAC address
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)

# Activate wlan0 network interface
subprocess.call("ifconfig wlan0 up", shell=True)
