class Dog:
    def __init__(self, new_name):
        self.name = new_name
        self.__age = 0
        #定义了一个私有的属性，属性的名字是__age

    #同过内部定义的方法设置私有属性
    def set_age(self, new_age):
        if new_age > 0 and new_age <= 100:
            self.__age = new_age

        else:
            self.__age = 0

    #通过内部定义的方法调用返回私有属性
    def get_age(self):
        return self.__age


dog = Dog('小白')
#dog.age = -10
#dog.name = '小黑'
#print(dog.age)
#print(dog.name)

dog.set_age(10)#通过内部方法设置私有属性
#age = dog.get_age()
#dog.__age = -10

print(dog.get_age())#通过内部方法调用私有属性

print(dog.__age)#直接调用报错，对象不存在调用属性


