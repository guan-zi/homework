from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print('reader启动%s,父进程为%s'%(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('reader从Queue获取到的消息：%s'%q.get(True))

def writer(q):
    print('reader启动%s,父进程为%s'%(os.getpid(), os.getppid()))
    for i in 'dongge':
        q.put(i)

if __name__ == '__main__':
    print('%s start'%os.getpid())
    q = Manager().Queue()
    po = Pool()
    #使用阻塞模式创建进程，这样就不需要reader中使用死循环了，可以让writer完全执行
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print('%s End'%os.getpid())
