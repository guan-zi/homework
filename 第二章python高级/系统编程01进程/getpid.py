import os

rpid = os.fork()
if rpid < 0:
    print('fork调用失败。')

elif rpid == 0:
    #验证子进程返回值为0
    print('我是子进程%s,我是父进程%s'%(os.getpid(), os.getppid()))
   

else:
    print('我是父进程%s,我是子进程%s'%(os.getpid(), rpid))

print('父子进程都可以执行这里的代码')

