# -*- coding=utf-8 -*-
def func(functionName):
    print('----func---1----')
    def func_in():
        print('----func_in---1--')
        ret = functionName()
        print('----func_in----2--')
        return ret#把haha返回到17行处的调用

    print('---func---2---')
    return func_in

@func
def test():
    print('----test----')
    return 'haha'

print('----fengexian-----')

ret = test()
print('test return value is %s'%ret)
