
try:
    num = input('xxxxx')
    int(num)
    print('---1---')

except(NameError, FileNotFoundError):
    print('如果捕获异常后做的处理……')

except Exception as ret:
    print('如果用了Exception，那么意味着上面except没有捕获到的异常，这个except一定能或到')
    print(ret)

else:
    print('没有异常才会执行的功能')


finally:
    print('----finally---')#不管有没有异常都会执行

print('-------2-------')
