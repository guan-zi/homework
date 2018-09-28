def func(functionName):
    print('---func---1---')
    def func_in(*args, **kwargs):#采用不定长参数的方式满足所有函数需要参数以及不需要参数的情况
        print('---func_in---1---')
        functionName(*args, **kwargs)
        print('----func_in---2---')

    print('---func--2--')
    return func_in

@func
def test(a, b, c):
    print('----test-a=%d, b=%d, c=%d---'%(a, b, c))
print('----分割线---')
@func
def test2(a, b, c, d):

    print('----test-a=%d, b=%d, c=%d, d=%d---'%(a, b, c, d))

print('----分割线---')
test(11, 22, 33)
test2(44, 55, 66,77)
        
