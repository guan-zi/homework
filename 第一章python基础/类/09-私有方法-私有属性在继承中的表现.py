class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200


    def test1(self):
        print('------test1-------')


    def __test2(self):
        print('----test2-----')


    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    def test4(self):
        self.__test2() #父类的私有方法即使定义方法也无法被子类调用
        print(self.__num2)#父类的私有属性即使定义方法也无法被子类调用


b = B()
#b.test1()#可以继承
#b.__test2()#私有方法并不会被继承，运行报错
#print(b.num1)#可以继承
#print(b.__num2)#私有属性不能继承

b.test3()#通过继承的的方法对私有属性和私有方法进行调用
b.test4()




