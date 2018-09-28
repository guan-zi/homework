
from multiprocessing import Process
import time
import os

#继承Process类
class Process_Class(Process):
    #因为Process类本身也有__init__方法，这给类相当于重写了这个方法；
    #但这样就会带来一个问题，我们并没有完全初始化一个Process类，所以不能使用从这
    #最好的方法就是将继承类本身传递给Process.__init__方法，完成这些初始化
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    #重写了Process类的run()方法
    def run(self):
        print('子进程%s开始执行，父进程为%s'%(os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print('%s执行结束，耗时%0.2f秒'%(os.getpid(), (t_stop-t_start)))

if __name__ == '__main__':
    t_start = time.time()
    print('当前程序进程%s'%os.getpid())
    p1 = Process_Class(2)
    #对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法
    p1.start()
    p1.join()
    t_stop = time.time()
    print('%s执行结束，耗时%0.2f秒'%(os.getpid(), (t_stop-t_start)))
