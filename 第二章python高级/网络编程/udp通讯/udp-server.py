from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(('127.0.0.1', 7788))
recvData = udpsocket.recvfrom(1024)
print(recvData)



if __name__ == '__main__':
    main()
