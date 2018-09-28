import os
import time

pid = os.fork()
if pid == 0:
    print('hh1')
else:
    print('hh2')

pid = os.fork()
if pid == 0:
    print('hh3')
else:
    print('hh4')

time.sleep(1)
