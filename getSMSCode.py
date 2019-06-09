#encoding=utf-8
import redis
#98
pool = redis.ConnectionPool(host='hb-bp160v2vm95b33rio-003.hbase.rds.aliyuncs.com',port=2181,db=0,password='1231@#zaqXSW')
#139
#pool = redis.ConnectionPool(host='10.19.219.223',port=6379,db=0)
r=redis.Redis(connection_pool=pool)
print 'start'
keys=r.keys()
print keys
phone_number=raw_input('enter phone number:')
code_key='code_'+phone_number
code=''
for key in keys:
    if code_key in key:
        code = r.get(key)
        break
    
if(code):
    print code
else:
    print 'no code'
    