#-*- coding = utf-8 -*-
import socket
from multiprocessing import Process

def handle_client(client_socket):
    request_data = client_socket.recv(1024)
    print('request_data',request_data)
    response_start_line = 'HTTP/1.1 200 OK'
    response_headers ='Server: My Server/r/n'
    response_body = 'hello itcast'
    response = response_start_line + response_headers + '/r/n' +response_body
    print('response data', response)

    client_socket.send(bytes(response, encoding='utf-8'))

    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8000))
    server_socket.listen(128)

    while True:
        print('------line1-----')
        client_socket, client_addr = server_socket.accept()
        print('-----line2----')
        print('[%s:%s]user connected!'%client_addr)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
if __name__ == '__main__':
    main()