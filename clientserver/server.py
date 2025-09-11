"""
server.py

Server Application
The server will:

Receive input in the form of a string, consisting solely of digits. If the
received string contains any non-digit character, the server will return an
error code to the client and terminate. Perform a digit sum on the number. Send
the digit sum result to the client. Terminate if the input is a single digit
long.
"""

import json
import socket

from constants import *  # Import HOST and PORT values

print("server starting")

# Create a TCP socket using IPv4 and stream-based communication
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the server to the specified host and port
    s.bind((HOST, PORT))
    print(f"Server Socket: {s.getsockname()}")

    # Listen for incoming client connections (backlog defaults to system)
    s.listen()

    # Accept a client connection (blocking until one connects)
    conn, addr = s.accept()
    with conn:
        # Keep processing data until a termination condition is reached
        while True:
            # Receive up to 1024 bytes of data from the client, decode as UTF-8
            data = conn.recv(1024).decode("utf-8")

            # Default JSON response template
            response = {"data": data, "status": "ok"}

            # Validate input: ensure it only contains digits
            if not data.isdigit():
                response["status"] = "Input data is not a digit"
                break  # Stop processing and terminate the server loop

            # If input is a single digit, stop processing
            if len(data) <= 1:
                response["status"] = "Input data is a single digit"
                break

            # Compute digit sum (e.g., "1234" → 1+2+3+4 = 10)
            output = 0
            for i in data:
                output += int(i)
            response["data"] = str(output)  # Store result as a string

            # If client sent nothing, close connection
            if not data:
                break

            # Send response JSON back to client
            # Example response:
            #   {"data": "10", "status": "ok"}
            conn.sendall(json.dumps(response).encode())
