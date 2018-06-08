import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(HOST, PORT)
if data == s.recv(50007):
    data = s.recv(1024)
print('Received', repr(data))
