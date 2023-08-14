import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for connections...")

# Accept a connection
client_socket, client_address = server_socket.accept()

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received: {data}")

# Send a response back to the client
response = "Hello from the server!"
client_socket.send(response.encode())

# Close the sockets
client_socket.close()
server_socket.close()
