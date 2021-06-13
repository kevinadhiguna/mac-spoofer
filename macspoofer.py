import subprocess
import optparse

# Create an instance for the OptionParser
parser = optparse.OptionParser()

parser.add_option(
  "-i", "--interface",  # A parameter which will be initialized before storing a network interface name.
  dest="interface",     # Store the value that comes after '-i' or '--interface' to a variable called 'interface'.
  help="A network interface name whose MAC address will be changed" # If a user needs help. please display this to explain what '-i' and '--interface' are for.
)

parser.add_option(
  "-m", "--mac",              # A parameter which will be initialized before storing a new MAC address.
  dest="new_mac_address",     # Store the value that comes after '-m' or '--mac' to a variable called 'new_mac_address'.
  help="A new MAC address"    # If a user needs help. please display this to explain what '-m' and '--mac' are for.
)

# 'parse_args()' will return options(e.g.: -i, --mac) and arguments(e.g.: 'wlan0', '00:11:22:33:44:55')
(options, arguments) = parser.parse_args()

# Set name of interface to 'dest' in interface option
interface = options.interface

# Set a new MAC address to 'dest' in new MAC address option
new_mac_address = options.new_mac_address

# -- for Python 2.7 --
# interface = raw_input("network interface > ")
# new_mac_address = raw_input("new MAC address >")

print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

# Run 'ifconfig wlan0 down' command in shell to deactivate a network interface named wlan0
subprocess.call(["ifconfig", interface, "down"])

# Changing MAC address
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])

# Activate wlan0 network interface
subprocess.call(["ifconfig", interface, "up"])
