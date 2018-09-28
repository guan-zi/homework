# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('子进程运行中，name=%s,子进程pid=%d, 父进程ppid=%d---'%(name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('父进程 %d'%(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('子进程将要执行')
    p.start()
    p.join()
    print('子进程已结束')
