import socket

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("UDP server is listening on", HOST, PORT)

data, addr = server_socket.recvfrom(1024)  # Receive data from client
print("Received from client:", data.decode())

response = "Hello from the UDP server!"
server_socket.sendto(response.encode(), addr)
