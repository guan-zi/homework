from socket import *
from threading import Thread
from multiprocessing import Lock
import time


# 发送信息方法
def server_s_msg():
    # 持续接收键盘输入信息如果，接收到字符串‘0’退出方法
    while True:
        lock.acquire()
        global flag
        if sendDest == None:
            lock.release()
            flag = True
            continue
        else:
            sendmsg = input('<发送的信息为(0:退出)：')
            if sendmsg == '0':
                udpsocket.sendto(sendmsg.encode('utf-8'), sendDest)
                lock.release()
                break
            else:
                #udpsocket.sendto(sendmsg.encode('utf-8'), sendDest)
                udpsocket.sendto(sendmsg.encode('utf-8'), sendDest)
                lock.release()
                break

# 接收信息方法
def server_r_msg():
    def recv_msg():
        global recv_Data
        recv_Data = udpsocket.recvfrom(1024)
        return recv_Data

    while True:
        lock.acquire()  # 加锁，如果上锁，判断是否接收到信息，如果没有开锁
        
        global recv_Data
        
        # recv_Data = udpsocket.recvfrom(1024)
        thread_re = Thread(target=recv_msg)
        thread_re.start()
        # time.sleep(0.1)
        thread_re.join()
        if recv_Data == '':
            lock.release()
            continue
        else:
            # 约定如果接收到字符串‘0’方法结束，否则持续打印接收到的信息
            # if recv_Data[0].encocde('utf-8') == '0':
            if recv_Data[0] == b'0':
                lock.release()
                break
            else:
                print('>>%s:%s' % (str(recv_Data[1]), recv_Data[0].decode('utf-8')))
                global sendDest
                sendDest = recv_Data[1]
                print(sendDest)
                lock.release()
                continue


# send_ip = ''
# send_port = None
recv_Data = ''
sendDest = None
udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(('127.0.0.1', 8000))
lock = Lock()
#flag = True

def main():
    # recv_Data = udpsocket.recvfrom(1024)
    # global send_ip = recv_Data[1][0]
    # global send_port = recv_Data[1][1]
    p_s_msg = Thread(target=server_s_msg)
    p_r_msg = Thread(target=server_r_msg)

    p_s_msg.start()
    p_r_msg.start()

    p_r_msg.join()
    p_s_msg.join()

    udpsocket.close()


if __name__ == '__main__':
    main()
