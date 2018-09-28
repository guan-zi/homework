import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.test
stu = db.stu
stu.insert({'name':'nandi','age':54})
stu.update({'name':'nandi'},{'$set':{'gender':1}})
s1 = stu.find()
for s in s1:
    print(s)
print(stu.count())