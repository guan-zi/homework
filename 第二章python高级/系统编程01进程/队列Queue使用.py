from multiprocessing import Queue

q = Queue(3)
q.put('消息1')
q.put('消息2')
print(q.full())
q.put('消息3')
print(q.full())
#因为消息对象列已满下面的try都会抛出异常，第一个try会等待2秒后再抛出异常，第2个会立即抛出异常。
try:
    q.put('消息4',True, 2)
except:
    print('消息队列已满，现有消息数量：%s'%q.qsize())

try:
    q.put_nowait('消息4')
except:
    print('消息队列已满，现有消息数量：%s'%q.qsize())

#推荐的方式，先判断队列是否已满，再写入
if not q.full():
    q.put_nowait('消息4')
if not q.empty():
    for i in range(q.qsize()):
        print(print(q.get_nowait()))
