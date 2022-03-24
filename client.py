# CSCE 3530 - Network Programming Assignment
# 03/24/2022
# Huy Anh Nguyen

import sys
from socket import *
from time import time

host = sys.argv[1]
port = int(sys.argv[2])

s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)
print("Name: Huy Anh Nguyen")
print("EUID: hn0135")

# Ping / send request 10 times
for i in range(10):
    message = "PING"
    print(f"{i+1} : sent {message}...", end='')

    try:
        # Send request to the server
        s.sendto(message.encode(), (host, port))

        # Receive data and decode 
        data, addr = s.recvfrom(1024)
        data = data.decode()

        print(f" recieved b'{data}'")
    except:
        print(f" Timed Out\n")

s.close()
