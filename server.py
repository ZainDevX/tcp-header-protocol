import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to localhost and port
server_socket.bind(('127.0.0.1', 65432))

# Put socket into Passive state
server_socket.listen()

print("Server is in PASSIVE state, waiting for connection...")

# Accept client connection
conn, addr = server_socket.accept()

print(f"Connection established with client: {addr}")

# Receive the 3-byte header first
header = conn.recv(3)

# Convert header from bytes to string, then to integer
message_length = int(header.decode())

print(f"Message length received: {message_length} bytes")

# Receive the actual message
data = conn.recv(message_length)

# Convert bytes to string
message = data.decode()

print(f"Received message: {message}")

# Close connection
conn.close()
server_socket.close()

print("Connection closed.")