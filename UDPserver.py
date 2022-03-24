# CSCE 3530 - Network Programming Assignment
# 03/24/2022
# Huy Anh Nguyen

from socket import *
import random

# IP is set to local, port 10000
ipAddress = '127.0.0.1'
port = 5050

# Use UDP(SOCK_DGRAM) socket
s = socket(AF_INET, SOCK_DGRAM)

s.bind((ipAddress, port))

while(True):

    # Message and address of the packet from client
    data, addr = s.recvfrom(1024)

    # Generate a random number form 1-10 to "drop" 30% of the packet
    dropRate = random.randint(1, 10)

    if dropRate  < 4:
        continue
    else:
        s.sendto(data, addr)
