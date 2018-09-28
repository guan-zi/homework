
def makeBold(fn):
    def wrapped():
        print('---1---- ')
        return '<b>'+fn()+'</b>'
    return wrapped


def makeItalic(fn):
    def wrapped():
        print('----2----')
        return '<i>'+fn()+'</i>'
    return wrapped


@makeBold
@makeItalic
def test3():
    print('-----3----')
    return 'hello world-03'

ret = test3()
print(ret)

