from threading import Thread
from socket import *

#1.sendmsg
def sendmsg():
	while True:
		s_msg = input('<<message:')
		udpSocket.sendto(s_msg, (s_ip,s_port))

#2.recvmsg
def recvmsg():
	while True:
		r_msg = udpSocket.recvfrom(1024)
		print('>>%s:%s'%(str(r_msg[1]).encode('utf-8'), r_msg[0]))

udpSocket = None
s_port = 0
s_ip = ''

#3.main()
def main():
	global udpsocket
	global s_ip
	global s_port

	s_ip = input('<<reciveip:')
	s_port = int(input('<<reciveport:'))

	udpsocket = socket(AF_INET, SOCK_DGRAM)
	udpSocket.bind(('127.0.0.1', 8000))

	ts = Thread(target = sendmsg)
	tr = Thread(target = recvmsg)

	ts.start()
	tr.start()

	ts.join()
	tr.join()

if __name__ == '__main__':
	main()
