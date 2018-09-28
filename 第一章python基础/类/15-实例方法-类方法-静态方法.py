class Game(object):

    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = 'laowang'

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100


    #静态方法
    @staticmethod
    def print_menu():
        print('----------------')
        print('   穿越火线v11.1')
        print('1.开始游戏')
        print('2.结束游戏')
        print('----------------')

game = Game()
#Game.add_num()#可以通过类的名字调用类的方法

game.add_num()#还可以通过这个类创建的对象去掉用这个类的方法。
print(Game.num)
print(game.num)
#Game.print_menu()#通过类去调用静态方法
game.print_menu()#通过实例对象去调用静态方法






    
