#1打印功能显示
print('='*50)
print('名片管理系统 v0.01'.cent(50, ''))
print('1.添加一个新的名片')
print('2.删除一个名片')
print('3.修改一个名片')
print('4.查询一个名片')
print('5.退出系统')
print('='*50)

#用来存储名片
card_info = []

while True:
    #获取用户的输入

    num = int(input('请输入操作序号：'))

    #根据用户的数据执行相应的功能
    if num == 1:
        new_name = input('请输入新的名字：')

        new_qq = input('请输入新的QQ：')

        new_weixin = input('请输入新的微信：')

        new_addr = input('请输入新的住址:')

        #定义一个新的字典，用来存储一个新的名片
        new_info = {}
        new_info['name'] = new_name
        new_info['qq'] = new_qq
        new_info['weixin'] = new_weixin
        new_info['addr'] = new_addr

        card_info.append(new_info)
        print(card_info)
    elif num == 2:
        pass

    elif num == 3:
        pass

    elif num == 4:
        pass
    
    elif num == 5 :
        break

    else:
        print('输入有误，请重新输入')
