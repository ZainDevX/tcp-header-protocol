# TCP Header Protocol

A simple Python client-server application that demonstrates TCP socket communication and implements a 3-byte message length header protocol.

## Overview

TCP provides reliable and ordered communication, but it treats data as a continuous byte stream rather than separate messages.

Because of this, using a fixed buffer such as `recv(16)` may not be enough when the message is longer than 16 bytes.

This project solves this problem by sending a **3-byte header containing the message length before the actual message**.

### Communication Flow

```text
Client
   |
   |  3-byte message length
   |  "055"
   |
   |  Actual message
   |  "Hello, this is a long TCP..."
   v
Server
```

The server first reads the 3-byte header, determines the message length, and then receives the specified number of bytes.

## Features

- TCP client-server communication
- Python `socket` module
- IPv4 (`AF_INET`)
- TCP sockets (`SOCK_STREAM`)
- 3-byte message length header
- Support for messages longer than 16 characters
- Separate client and server programs
- Simple request-response communication

## Project Structure

```text
tcp-header-protocol/
│
├── client.py
├── server.py
├── README.md
│
└── screenshots/
    ├── client-output.png
    └── server-output.png
```

## How the Protocol Works

The client performs the following steps:

1. Creates a TCP socket.
2. Connects to the server.
3. Calculates the message length.
4. Converts the length into a 3-digit string using `.zfill(3)`.
5. Sends the 3-byte header.
6. Sends the actual message.

The server performs the following steps:

1. Creates a TCP socket.
2. Binds to the local IP address and port.
3. Starts listening for connections.
4. Accepts the client connection.
5. Receives the 3-byte header.
6. Converts the header into an integer.
7. Receives the exact number of bytes specified by the header.
8. Displays the complete message.

## Example

### Test Message

```text
Hello, this is a long TCP Header Protocol test message!
```

The message is longer than 16 characters, allowing the Header Protocol to be tested against the fixed `recv(16)` limitation.

### Header

The message length is converted into a 3-digit value.

```text
055
```

The client sends the header first, followed by the actual message:

```text
[055][Hello, this is a long TCP Header Protocol test message!]
```

The server reads the 3-byte header first and then uses the received length to read the complete message.

## Requirements

- Python 3.x
- No external Python packages are required.

## Running the Project

### 1. Start the Server

Open a terminal and run:

```bash
python server.py
```

The server will wait for an incoming connection.

### 2. Start the Client

Open a second terminal and run:

```bash
python client.py
```

The client will connect to the server and send the test message.

### 3. Verify the Output

The server should display the received message and its length.

Example:

```text
Server is in PASSIVE state, waiting for connection...
Connection established with client
Message length received: 55 bytes
Received message: Hello, this is a long TCP Header Protocol test message!
Connection closed.
```

## Test Results

The Header Protocol was tested using a message longer than 16 characters.

### Client Output

The client calculates the message length, creates the 3-byte header, and sends the header followed by the message.

<img src="https://github.com/user-attachments/assets/681342b3-3517-4db4-8196-80d997b87bf5" width="700">

### Server Output

The server receives the 3-byte header, determines the message length, and receives the complete message.

<img src="https://github.com/user-attachments/assets/01184960-c027-4372-aa60-04b99bc75ba2" width="700">

## Technologies Used

- Python
- TCP
- IPv4
- Python Socket API

## Learning Objectives

This project demonstrates:

- Basic TCP socket programming
- Client-server architecture
- Passive and active socket states
- TCP data streams
- Message length framing
- Sending and receiving byte data
- Converting between strings and bytes

## Why the Header Protocol Is Required

TCP is a stream-oriented protocol and does not provide message boundaries.

If the server uses:

```python
conn.recv(16)
```

it may receive only the first 16 bytes of a longer message while the remaining bytes stay in the operating system buffer.

The 3-byte Header Protocol solves this problem by sending the message length before the actual message. The server first reads the 3-byte header and then receives the specified number of bytes.

## Conclusion

The 3-byte Header Protocol provides a simple way to define message boundaries when using TCP.

By sending the message length before the actual message, the server knows how many bytes it needs to receive and can correctly handle messages longer than a fixed buffer size.
