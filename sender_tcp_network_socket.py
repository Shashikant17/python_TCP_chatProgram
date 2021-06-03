import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = str(input("Enter Receiver IP: "))
port = 1234
s.connect( (ip,port) )

msgs = input("Enter your message: ").encode()
s.send(msgs)

msgr = s.recv(1024)
print(msgr.decode())
