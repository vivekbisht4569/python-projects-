#!/usr/bin/env python3
import socket

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid domain or host")
    exit()

print("Scanning:", target_ip)

for port in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()


