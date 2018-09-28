from socket import *

def main():
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(('127.0.0.1', 7788))
    while True:
        recvData = udpsocket.recvfrom(1024)
        print('>>%s:%s'%(recvData[1], recvData[0].decode('utf-8')))
        sendmsg = input('<<:')
        if sendmsg != '':
            udpsocket.sendto(sendmsg.encode('utf-8'), recvData[1])


if __name__ == '__main__':
    main()
