from socket import *
from threading import Thread, Lock


def client_send_msg():
    lock.acquire()
    while True:
        sendmsg = input('<发送的信息为：')
        udp_client_socket.sendto(sendmsg.encode('utf-8'),sendDest)
        lock.release()

def client_recv_msg():

    lock.acquire()
    while True:
        client_recv_Data = udp_client_socket.recvfrom(1024)
        print('>>%s:%s'%(str(client_recv_Data[1]), client_recv_Data[0].decode('utf-8')))
        lock.release()

lock = Lock()
udp_client_socket = socket(AF_INET, SOCK_DGRAM)
sendDest = ('127.0.0.1', 8000)

def main():
    
    client_send_thread = Thread(target=client_send_msg)
    client_recv_thread = Thread(target=client_recv_msg)

    client_send_thread.start()
    client_recv_thread.start()
    
    client_send_thread.join()
    client_recv_thread.join()

    udp_client_socket.close()


if __name__ == '__main__':
    main()
