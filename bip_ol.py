#encoding=utf-8
import socket
import time
import json
import os
import subprocess
import re

key_list=[
          'A','B','C','D','E','F','G','vt','vvid','vst','p','st','Y5','sc','sds','nt','ver','ci','tec','dp',
          'ft','bwt','isp','sectionid','DM','usr'

          ]

print len(key_list)
param='A=0&B=867080022782696&C=29549639&D=%E3%80%8A%E5%B0%8F%E5%A5%B3%E8%8A%B1%E4%B8%8D%E5%BC%83%E3%80%8B%E4%B8%8D%E5%BC%83%E5%88%B7%E7%94%9F%E5%AD%98%E5%89%AF%E6%9C%AC%EF%BC%8C%E5%BE%92%E6%89%8B%E6%8A%93%E8%80%81%E9%BC%A0%E6%AC%B2%E7%94%9F%E5%90%83&E=0&F=&G=1547193449433&vt=92688&vvid=2ba26d9f-10bb-472b-ad8b-28ffc7be71cf&vst=0&p=5&Y5=74:51:ba:eb:f0:46&sc=0&sds=0&nt=0&ver=7.4.7&ci=114.80.186.142&tec=4&dp=0&ft=0&bwt=0&DM=1&usr=&st=1547193449433&isp=0&sectionid=0'

temp_list=param.split('&')
send_list=[]
pattern=re.compile(r'(\S+)=')
for item in temp_list:
    if '=' in item:
        send_list.append(pattern.findall(item)[0])
    else:
        send_list.append(item)
for item in key_list:
    if not item in send_list:
        print item
print send_list

#print len(param_dict),len(ext_dict)
