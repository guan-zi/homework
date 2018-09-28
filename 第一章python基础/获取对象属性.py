class  Cat:
	#属性
    def __init__(self):
        print('----haha---')
	#方法
    def eat(self):

    	print('猫在吃鱼%s'%self)
	

    def drink(self):
	print('猫在喝水%s'%self)



    def introduce(self):
        print('%s的年龄是%d'%(self.name, self.age))
#创建一个对象
tom = Cat()

tom.eat()

tom.drink()
tom.name = '汤姆'
tom.age = '46'
#相当于为对象添加属性

print('%s的年龄是%d'%(tom.name, tom.a语言ge))
#获取属性的第一种方法








