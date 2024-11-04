import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello from the UDP client!"
client_socket.sendto(message.encode(), (HOST, PORT))

data, server = client_socket.recvfrom(1024)
print("Received from server:", data.decode())
