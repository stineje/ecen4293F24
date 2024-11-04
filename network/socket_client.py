import socket

# Define the server's IP address and port
HOST = '127.0.0.1'  # Server's IP address
PORT = 65432        # Server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send data to the server
message = "Hello from the client!"
client_socket.sendall(message.encode())

# Receive data from the server
data = client_socket.recv(1024)
print("Received from server:", data.decode())

# Close the connection
client_socket.close()
