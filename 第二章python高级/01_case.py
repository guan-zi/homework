from socket import *
from multiprocessing import Process

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind('', 8000)
server_socket.listen(128)
client_socket = server_socket.accept()

while True:
	p = Process(target=fun, args=())
	p.start()
	client_socket.close()

def fun(client_socket):
	request_data = client_socket.recv()
	print(request_data)

	