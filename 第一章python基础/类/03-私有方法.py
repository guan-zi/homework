class Dog:


    #私有方法
    def __send_msg(self):
        print('-------正在发送短信-------')


    #公有方法
    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print('余额不足，请先充值，自发短信……')


dog = Dog()

dog.send_msg(1000)#不满足判断条件无法调用私有方法
dog.send_msg(100000)#成功调用私有方法
dog.__send_msg()#报错无法直接调用，显示不存在方法


