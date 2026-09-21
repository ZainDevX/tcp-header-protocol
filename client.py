import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('127.0.0.1', 65432))

# Message longer than 16 characters
message = "Hello, this is a long TCP Header Protocol test message!"

# Calculate message length
message_length = len(message)

# Create 3-byte header
header = str(message_length).zfill(3)

print(f"Message: {message}")
print(f"Message length: {message_length} bytes")
print(f"Header: {header}")

# Send the 3-byte header first
client_socket.send(header.encode())

# Send the actual message
client_socket.send(message.encode())

print("Header and message sent successfully.")

# Close connection
client_socket.close()