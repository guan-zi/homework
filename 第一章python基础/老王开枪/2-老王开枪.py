class Person(object):
    """人的类"""
    def __init__(self, name):
        super(Person, self).__init__()
        #有可能调用父类的功能，但不一定用
        self.name = name


class Gun(object):
    """枪类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name#用来记录枪的类型


class Danjia(object):
    """弹夹类"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.name = name
        self.max_num = max_num#用来记录弹夹的最大容量

class Zidan(object):
    """子弹类"""
    def __init__(self, sha_shang_li):
        super(Person, self).__init__()
        self.sha_shang_li  = sha_shang_li#这颗子弹的威力







def main():
    """用来控制整个程序的流程"""
    pass

    #1.创建老王对象
    laowang = Person('老王')

    #2.创建一个枪对象
    ak47 = Gun('AK47')

    #3.创建一个弹夹对象
    dan_jia = Danjia(20)


    #4.创建一些子弹
    zi_dan = Zidan(10)


    #5.老王把子弹装到弹夹中
    laowang.anzhuang_zidan(dan_jia, zidan)

    #6.老王把弹夹装到枪中

    #7.老王拿枪


    #8.创建一个敌人


    #9.老王开枪大敌人













if __name__ == '__main__':
    main()

