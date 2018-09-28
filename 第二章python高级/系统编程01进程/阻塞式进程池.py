from multiprocessing import Pool
import os
import time
import random

def worker(msg):
    t_start = time.time()
    print('%s开始执行，进程号为%d'%(msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,'执行完毕，耗时%0.2f'%(t_stop-t_start))

po = Pool(3)
for i in range(0, 10):
    #Pool.apply_async(要调用的目标，（传递给目标的参数元组，）)
    #每次循环将会用空闲出来的子进程去调用目标
    po.apply(worker, (i,))

print('----start----')
po.close()#关闭进程池，关闭后po不再接受新的请求
po.join()#等待po中所有的子进程执行完成，必须放在close语句之后
print('----end------')
