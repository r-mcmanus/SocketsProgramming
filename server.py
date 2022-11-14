import socket

# A socket is an address and a port number

# This is the private address of the local host
# Can also put in a hard coded ip address string
HOST = socket.gethostbyname(socket.gethostname())

# if you're interested in hosting on this computer only
#HOST = 'localhost' or HOST = 127.0.0.1

# Don't use the well known port numbers
# Use same port for client and server
PORT = 9090


print(HOST)

# The first argument of the socket.socket function is an address type (IPv4)
#The second argument is the type, in this case TCP
#server is a socket object
#This socket is just for listing and accepting connections
#We create a separate socket for communicating with clients
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# .bind takes a tuple of host and port
server.bind((HOST, PORT))
# it's waiting and limiting the number of connections I think, before it starts looping
server.listen(5)

while True:
    server.accept()
    communication_socket, address = server.accept() #Do nothing while waiting for connections to come in
    #We use communication_socket to talk to the client, address is the address of the client
    #Each connection creates a new socket
    #The server socket is only for accepting connections
    print(f'Connected to {address}')
    #specify buffer size and decode byte stream
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from client is {message}')
    communication_socket.send(f'Got your message! Thank you!'.encode('utf-8'))
    communication_socket.close()
    print(f'Connection with {address} ended!')