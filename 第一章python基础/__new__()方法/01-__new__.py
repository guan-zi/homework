class Dog(object):
    def __init__(self):
        print('-------init方法-----')
    
    def __del__(self): 
        print('----del方法--------')

    def __str__(self):
        print('-------str方法-----')

    def __new__(cls):#cls此时是Dog指向的那个类对象
        print(id(cls))
        
        print('-----new方法-----')
        return object.__new__(cls)

print(id(Dog))
xtq = Dog()
#创建一个对象相当于要做三件事：
#1、调用__new__方法来创建对象，然后找了一个变量来接收__new__的返回值，这个返回值表示创建出来的对象引用
#2、__init__初始化对象（刚刚创建出来的对象的应用）
#3、返回对象的引用




