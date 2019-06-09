#encoding=utf-8
from hyper import HTTPConnection,tls
import json
#from jwt import JWT
import jwt
import time

token='5bf101506517f089fa8cd6225978420b5385623c41a01f7c5a3d6c47c243d21c'
production=True
#production=False
#jwt=JWT()
payload={
         "aps": {
               "sound": "default",
               "mutable-content": 1,
               "badge": 1,
               "alert": {
                       "body": "为什么你是神仙我是凡人为什么我们还能生孩",
                       "action-loc-key": "播放",
                       }
               },
        #云信
        
        'action': "pptv://player/?sid=26874955&vid=26874955&type=ppvod",
        #'action': "pptv://page/usercenter",
        'actionType': 3,
        'actionParam': "{\"pushid\":\"123123\"}"
        
        #个推
        
         #"pptv":{
         #        
         #       "url":"pptv://page/usercenter",
         #       "videoid":21456489,
         #       "image": "http://pic.58pic.com/58pic/11/67/63/91r58PICKiw.jpg",
         #       "id": 311,
        #      "type": 7
        #      }  
         
         }
        



with open('APNsAuthKey_3HX434X7XP.p8') as f:
    secret_key=f.read()
apns_keyid='3HX434X7XP'
apns_teamid='3U62SP5YP3'
#iphone
#bundle_id='com.pptv.iphoneapp'
#ipad
bundle_id='com.pptv.ipadwebkit'
algorithm='ES256'
authorization_token=jwt.encode({
                               'iss': apns_teamid,
                               'iat': time.time()
                                
                                },
                               secret_key,
                               algorithm=algorithm,
                               headers={
                                'alg':algorithm,
                                'kid':apns_keyid
                                        
                                }                             
                               )

request_headers = {
            'apns-expiration': '0',
            'apns-priority': '10',
            'apns-topic': bundle_id,
            'authorization': 'bearer {0}'.format(authorization_token.decode('ascii'))
        }
#print authorization_token
if production:
    apns_server='api.push.apple.com:443'
else:
    apns_server='api.development.push.apple.com:443'
conn=HTTPConnection(apns_server)
conn.request('POST', '/3/device/%s' % token, bytes(json.dumps(payload).strip('')), headers=request_headers)

resp=conn.get_response()

errorinfo=resp.read()
if errorinfo:
    print('error')
else:
    print('push successfully')
print bytes(json.dumps(payload).strip())
