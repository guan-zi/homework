#-*- coding=utf-8 -*-
import redis

try:
    r = redis.StrictRedis(host='localhost', port=6379)
except Exception as e:
    print(e)

r.set('name', 'hanmeimei')
r.get('name')
