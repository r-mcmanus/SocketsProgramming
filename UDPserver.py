import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 12345))

while True:
    data, addr = s.recvfrom(4096)
    print(str(data.decode('utf-8')))
    message = bytes('Hello, I am a UDP server!'.encode('utf-8'))
    s.sendto(message, addr)