import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = str(input("Enter receiver IP: "))
port = 1234

s.bind((ip,port))

s.listen()

# any sender come memorize it. --> "maintain connection"
connection , address = s.accept()

msgr = connection.recv(1024)
print(msgr.decode())


msgs = input("Enter your message: ").encode()
connection.send(msgs)
