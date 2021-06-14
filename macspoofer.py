import subprocess
import optparse
import re

def get_arguments():
  """
  A function to get arguments.
  """
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
  (options, argumemnts) = parser.parse_args()

  # Error handling
  if not options.interface:
    parser.error("[-] Please specify a network interface! You can use '--help' for more options.")
  elif not options.new_mac_addres:
    parser.error("[-] Please specify a new MAC address! You can use '--help' for more options.")
  return options

def spoof_mac_address(interface, new_mac_address):
  """
  A function to spoof MAC address.
  """
  print("[+] Changing the MAC address for " + interface + " to " + new_mac_address + " ...")

  # Run 'ifconfig wlan0 down' command in shell to deactivate a network interface named wlan0
  subprocess.call(["ifconfig", interface, "down"])
  
  # Changing MAC address
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
  
  # Activate wlan0 network interface
  subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()

# Call the function to change MAC address and passing the required arguments
spoof_mac_address(options.interface, options.new_mac_address)

def get_current_mac_address(interface):
  """
  a function to get current MAC address
  """
  # Display a changed MAC address
  ifconfig_result = subprocess.check_output(["ifconfig", interface])

  # Regular Expression pattern for MAC address in ifconfig command
  mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

  # Error handling to make sure whether the network interface has a MAC address or not (e.g. : 'lo' is a network interface but it has no MAC address).
  if mac_address_search_result:
    # Display the first occurrence of the search result
    return mac_address_search_result.group[0]
  else:
    print("[-] Oops... could not read MAC address. Please check your network interface name and try again.")

# Call the function to get current MAC address and display it
current_mac_address = get_current_mac_address(options.interface)
print("[+] Voila! This is the spoofed MAC address : " + current_mac_address)
