import threading
import time

def test(i):
    print('昨天喝太多了我要戒酒……%d'%i)
    time.sleep(1)

for i in range(5):
    t = threading.Thread(target=test,args=(i,))
    t.start()
