from socket import *

def main():
    udp_client_socket = socket(AF_INET, SOCK_DGRAM)
    sendDest = ('127.0.0.1', 8000)
    while True:
        sendmsg = input('<发送的信息为：')
        udp_client_socket.sendto(sendmsg.encode('utf-8'),sendDest)
        client_recv_Data = udp_client_socket.recvfrom(1024)
        print('>>%s:%s'%(str(client_recv_Data[1]), client_recv_Data[0].decode('utf-8')))


if __name__ == '__main__':
    main()
