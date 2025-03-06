import subprocess
import random
import re
import argparse

def get_current_mac(interface):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    mac_address_search = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result.stdout)

    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[-] Could not read MAC address.")
        return None

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])

def generate_random_mac():
    return ":".join(["{:02x}".format(random.randint(0, 255)) for _ in range(6)])

def main():
    parser = argparse.ArgumentParser(description="MAC Address Changer")
    parser.add_argument("--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("--mac", help="Specify a new MAC address")
    parser.add_argument("--random", action="store_true", help="Generate a random MAC address")
    parser.add_argument("--restore", action="store_true", help="Restore original MAC address")
    parser.add_argument("--check", action="store_true", help="Check current MAC address")

    args = parser.parse_args()

    if args.check:
        current_mac = get_current_mac(args.interface)
        if current_mac:
            print(f"Current MAC: {current_mac}")
        return

    if args.restore:
        print("[+] Restoring original MAC address is not supported yet.")
        return

    new_mac = args.mac if args.mac else generate_random_mac() if args.random else None

    if new_mac:
        change_mac(args.interface, new_mac)
        print(f"[+] MAC address changed successfully to {new_mac}")
    else:
        print("[-] Please specify a MAC address or use --random.")

if __name__ == "__main__":
    main()
