#-*- coding = utf-8 -*-
import socket
import re

from multiprocessing import Process

# set static web directry
HTML_ROOT_DIR = './html'


def handle_client(client_socket):
    '''handle client request'''
    # get user request information

    request_data = client_socket.recv(1024)
    print('request_data',request_data.decode('utf-8'))
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)

    # anlysis request 
    # GET / HTTP/1.1
    request_start_line = request_lines[0]
    #get user request filename
    print('*'*10)
    print(request_start_line.decode('utf-8'))
    file_name = re.match(r'\w+ +(/[^ ]*)', request_start_line.decode('utf-8')).group(1)

    if '/' == file_name:
        file_name = '/index.html'

    #open file and read content
    try:
        file = open(HTML_ROOT_DIR + filename, 'rb')
    except:
        response_start_line = 'HTTP/1.1 404 Not Found\r\n'
        response_headers = 'Server: My server\r\n'
        response_body = 'The file is not found'
    else:
        file_data = file.read()
        file.close()
        
        # contribute response data 
        response_start_line = 'HTTP/1.1 200 OK'
        response_headers ='Server: My Server/r/n'
        response_body = file_data.decode('utf-8')

    response = response_start_line + response_headers + '/r/n' +response_body
    print('response data', response)

    # send response data to client
    client_socket.send(bytes(response, encoding='utf-8'))
    #close client connect
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RESUMEADDR, 1)
    server_socket.bind('', 8000)
    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        print('[%s:%s]user connected!'%client_addr)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
if __name__ == '__main__':
    main()