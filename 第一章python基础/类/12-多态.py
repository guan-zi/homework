class Dog(object):
    def print_self(self):
        print('大家好我是xxx，希望以后大家多多关照……')


class Xiaotq(Dog):
    def print_self(self):
        print('hello everybody，希望以后大家多多关照……')


def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)

introduce(dog2)

