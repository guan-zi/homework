class Store(object):

    def select_car(self):
        pass
    def order(self, car_type):
        return self.select_car(car_type)

class BMWCarStore(Store):
    def select_car(self, car_type):
        return BMWFactory().select_car_by_type(car_type)


class BMWFactory(object):
    def select_car_by_type(self, car_type):
        pass


bmw_store = BMWCarStore()
bmw = bmw_store.order('720li')


class CarStore(object):
    
    def select_car(self, car_type):
        return Factory().select_car_by_type(car_type)
        

class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == '索纳塔':
            return Sonata()

        elif car_type == '名图':
            return Mingtu()

        elif car_type == 'Ix35':
            return Ix35()


class Car(object):
    def move(self):
        print('车在移动……')

    def music(self):
        print('正在播放音乐……')

    def stop(self):
        print('车在停止……')

class Sonata(Car):
    pass


class Mingtu(Car):
    pass

class Ix35(Car):
    pass

car_store = CarStore()
#创建对象car_store--->对象初始化__init__(self)--->car_store.factory=Factory()---->创建第二个对象--->car_store.factory指向Factory()对象
car = car_store.select_car('索纳塔')
#通过car_store-->Factory-->调用select_car_by_type方法
car.move()
car.music()
car.stop()


