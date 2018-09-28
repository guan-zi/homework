from multiprocessing import Process
import os
from time import sleep

#子进程要执行的代码
def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name=%s, age=%d, pid=%d--'%(name, age, os.getpid()))
        print(kwargs)
        sleep(0.5)

if __name__ == '__main__':
    print('父进程%d'%os.getpid())
    p = Process(target=run_proc, args=('test', 18), kwargs={'m':20})
    #创建子进程实例
    print('子进程将要执行')
    p.start()#开启子进程
    sleep(1)
    
   
    p.terminate()#子进程循环两次与主进程睡眠时间相同然后执行主进程此条语句，子进程终止。
    
    p.join()#等待子进程执行完后执行执行主进程
 
    print('子进程已结束')
