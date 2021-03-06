## UDP-Socket-Programming
### 03/24/2022 - UNT

### Description: 
- A small program to demonstrate how UDP works. Created for CSCE 3530 Network Programming Assignment.

### How-to-run:
- Both server.py and client.py take 2 arguments, host name and port number.
- Usage: server.py <host_name> <port_number> / client.py <host_name> <port_number>
- e.g. python3 server.py 127.0.0.1 5050

### Requirements:
1. Client:
- Create a UDP socket (hostname and port are command line arguments or hard coded).
- Send 10 (probably in a loop) 'PING' message (hint: messages are bytes objects.
- Wait for the response back from the server for each with a timeout (see settimeout()
- If the server times out report that to the console, otherwise report the 'PONG' message recieved
2. Server:
- Create a UDP socket and bind it to the hostname of your machine and the same port as in the client (again either command line or hardcoded).
- Infinitely wait for a message from the client.
- When recieve a 'PING' respond back with a 'PONG' 70% of the time and artificially "drop" the packet 30% of the time (just don't send anything back).
- Server should report each ping message and each dropped packet to the console (just print it).

