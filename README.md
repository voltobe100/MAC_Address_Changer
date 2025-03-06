# MAC Address Changer – Spoof MAC Address using Python

## Overview

This tool allows users to change (spoof) their MAC address on Linux-based systems. Changing a MAC address can be useful for privacy, penetration testing, and bypassing certain network restrictions.

## Features

- Change MAC address of a selected network interface.
- Generate a random MAC address.
- Restore original MAC address.
- Verify the change.

## Installation

Ensure you have Python installed, then install required dependencies:

```bash
pip install argparse
```

## Usage

Run the script using the command:

```bash
sudo python mac_changer.py --interface eth0 --mac 00:11:22:33:44:55
```

### Additional Options

- Generate a random MAC address:
  ```bash
  sudo python mac_changer.py --interface eth0 --random
  ```
- Restore original MAC address:
  ```bash
  sudo python mac_changer.py --interface eth0 --restore
  ```
- Verify the MAC address change:
  ```bash
  sudo python mac_changer.py --interface eth0 --check
  ```

## Example Output

```bash
[+] Changing MAC address for eth0 to 00:11:22:33:44:55
[+] MAC address changed successfully!
```

## License

This project is licensed under the MIT License.
