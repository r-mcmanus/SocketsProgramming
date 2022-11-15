import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'Hello UDP server!'
s.sendto(message.encode('utf-8'), ('127.0.0.1', 12345))
data, addr = s.recvfrom(4096)
print('Server says: ')
print(str(data.decode('utf-8')))
s.close()