import sys
from socket import *
from time import time

host = sys.argv[1]
port = int(sys.argv[2])

s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)

# Ping / send request 10 times
for i in range(10):
    message = "Ping " + str(i+1)

    try:
        # Send request to the server
        s.sendto(message.encode(), (host, port))
        data, addr = s.recvfrom(1024)

        countTime = time()
        data = data.decode()
        print(data)
    except:
        print(f"Ping {i+1} timed out\n")

s.close()
