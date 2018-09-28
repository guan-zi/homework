from socket import *

udp_client_socket = socket(AF_INET, SOCK_DGRAM)
sendDest = ('127.0.0.1', 7788)
sendmsg = input('<发送的信息为：')
udp_client_socket.sendto(sendmsg.encode('utf-8'),sendDest)

