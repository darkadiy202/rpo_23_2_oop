import socket


host_name = socket.gethostname()
port = 12345

server = socket.socket()
server.bind(host_name, port)