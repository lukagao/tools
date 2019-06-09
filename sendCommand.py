#encoding=utf-8
import socket
import time
import json


print 'start'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind(('0.0.0.0',8006))
while True:
    try:
        s.connect(('10.200.106.98',5173))
        break;
    except IOError as e:
        if '10061'in str(e):
            continue
#print s.getsockname()
#print s.getpeername()

s.send('start'+'\n')
result=s.recv(1024).decode('utf-8')
print result

print 'connect successfully'
param={'objecttype':'uidevice',
        'uiobject':{'attr':'text','value':'联系人','index':'0'},
        'actiontype':'findObject',
        'findObject':{'attr':'text','value':'联系人'},                 
    }

param=json.dumps(param)
s.send(param+'\n')
result=s.recv(1024).decode('utf-8')
print result

paramclick={'objecttype':'uiobject',
        'uiobject':{'id':json.loads(result)['id'],'index':'0'},
        'actiontype':'click',
        'click':{'duration':0,},                 
    }
time.sleep(1)

paramclick=json.dumps(paramclick)
s.send(paramclick+'\n')
result=s.recv(1024)
if result:
    print result
else:
    print 'server end'



#print ('-->'+s.recv(1024).decode('utf-8'))
#s.send(b'exit')
time.sleep(1)
s.close()

