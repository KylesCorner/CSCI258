"""
client.py
The client will:

Request the Server’s IP Address and Port. Obtain the input string to send to
the server from the user. If the server returns an error code or a single digit
number, exit the client application. Send the returned results  back to the
server, and repeat until the server returns a single digit number.

"""

import json
import socket

from constants import *  # Import constants such as HOST and PORT

print("client starting")

# Prompt the user to input a number that will be sent to the server
msg = input("Type in a number: ")

# Create a TCP socket using IPv4 (AF_INET) and stream protocol (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server using HOST and PORT values from constants.py
    s.connect((HOST, PORT))

    # Display the client socket’s address (IP, port)
    print(f"Client Socket: {s.getsockname()}")

    # Send the user’s message (encoded as bytes) to the server
    s.sendall(msg.encode())

    # Receive up to 1024 bytes of data from the server, decode it, and parse JSON
    data = json.loads(s.recv(1024).decode())

    # Check if the response is too short (server returned a single character)
    if len(data) == 1:
        print("Data too short!")
        exit()

    # Check if the server returned an error (status != "ok")
    if data["status"] != "ok":
        print(f"Server Error: {data['status']}")
        exit()

# If everything is fine, print the server’s response
print(f"Data received: {data}")
