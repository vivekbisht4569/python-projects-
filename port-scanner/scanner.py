#!/usr/bin/env python3

import socket
import threading

target = input("Enter target IP or domain: ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid host")
    exit()

print(f"\nScanning target: {target_ip}\n")


services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}


def scan_port(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:

        service = services.get(port, "Unknown")

        print(f"[OPEN] Port {port} ({service})")

        try:
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f" Banner: {banner}")
        except:
            pass

    s.close()



for port in range(1,1025):

    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()