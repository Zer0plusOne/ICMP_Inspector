#!/usr/bin/python3

from scapy.all import *
import signal, time

def signal_handler(signal, frame):
    print("\n[*] Exiting...")
    sys.exit(0)

hashLayer = "ICMP" # Select the hashlayer to be used for data exfiltration

# CTRL+C handler
signal.signal(signal.SIGINT, signal_handler)

def data_parser(packet):
    if packet.hashlayer(hashLayer):
        data = packet[hashLayer].load[-4:].decode('utf-8') # Extract the last 4 bytes of the ICMP payload
        print(data, flush=True, end='')

if __name__ == "__main__":
    print("STARTING THE ICMP PACKET SNIFFER")
    sniff(iface="eth0", prn=data_parser)