class Base(object):#新式类推荐写法
    def test(self):
        print('-----Base-----')

class A(Base):
    def test1(self):
        print('----test1-----')

class B(Base):
    def test2(self):
        print('---test2----')


class C(A, B):
    pass


c = C()

c.test1()

c.test2()#可以有多个父类，可以全部继承父类们的公有方法

c.test()#可以继承父类的父类的公有方法。
