import socket

# Define the server's IP address and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()
print("Server is listening on", HOST, PORT)

# Accept a connection
conn, addr = server_socket.accept()
print("Connected by", addr)

# Receive data from the client
data = conn.recv(1024)
print("Received from client:", data.decode())

# Send a response to the client
response = "Hello from the server!"
conn.sendall(response.encode())

# Close the connection
conn.close()
