# CSCE 3530 - Network Programming Assignment
# 03/24/2022
# Huy Anh Nguyen

from socket import *
import random
import sys

# IP is set to local, port 10000
host = sys.argv[1]
port = int(sys.argv[2])

# Use UDP(SOCK_DGRAM) socket
s = socket(AF_INET, SOCK_DGRAM)

s.bind((host, port))

print("Name: Huy Anh Nguyen")
print("EUID: hn0135")
print("[server] : ready to accept data...")

while(True):

    # Message and address of the packet from client
    data, addr = s.recvfrom(1024)

    # Generate a random number form 1-10 to "drop" 30% of the packet
    dropRate = random.randint(1, 10)

    if dropRate <= 3: # 30% drop rate
        print("[server] : package dropped")
        continue
    else:
        print("[client] : PING")
        data = "PONG"
        s.sendto(data.encode(), addr)