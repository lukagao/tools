#encoding=utf-8
import socket
import time
import json
import os
import subprocess
import re

key_list=[
          'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','V','W',
          'Y1','Y2','Y3','Y4','Y5','Y6','D1','VVID','FT','FN','PM','PT','D3','D2','F1',
          'D5','FM','K1','L1','L3','M1','PW','PK','PD','W1','W2','AC','RL','R1','R2','R3','R4',
          'L4','RU','PM2','LB','W4','W5','ZT','S1','F','Tab','sectionid','yxid','PF','pvid','_IFID',
          '_CATAID1','_CATAID2','DPT','DM','RF','utm','RS'

          ]

print len(key_list)
param='FM=92000&R=0&AC=ARM64&S=1&W4&FN=1759&_CATAID2&W5&DPT&V=1777&PK=1&W=1&Y1=1002&RF&PM=2&Y2=iPhone%206SPlus&Y3=10.3.3&yxid&_IFID=9&Y4=1547259815&FT=2&LB&pvid&Y5=7EF13E8A-273F-42C2-98A6-AC79FB4B5F8B&R1&Y6&R2&RL=1242x2208&R3&R4&S1=0&PT=0&K1&PW=0&A=3&L1=1&sectionid&B=1&VVID=C994087D-C02C-4302-A015-2954DB4AE354&C&ZT&D1&D&PM2=2&L3&E&D2=cytestg&RS&F&M1=0&L4=0.000&D3&G=29549639&RU=http%3A%2F%2F127.0.0.1%3A9206%2Frecord.m3u8%3Fw%3D1%26key%3D4c7845bef5bdabfa3465ae3e4c7af401%26type%3Dppvod2%26sv%3D7.7.5%26platform%3Diphone4%26channel%3D1002%26ft%3D2%26accessType%3Dwifi%26vvid%3DC994087D-C02C-4302-A015-2954DB4AE354%26video%3Dtrue%26mux.M3U8.segment_duration%3D5%26chunked%3Dtrue%26serialnum%3D1%26playlink%3D29549639%253Fft%253D2%2526bwtype%253D0%2526platform%253Diphone4%2526type%253Dphone%252Eios%252Evip%2526sv%253D7%252E7%252E5%2526video%253Dtrue%2526sdkmode%253D0%2526p2p%252Eadvtime%253D0%2526k%253Da9a478c0cf638171d2573876f3e1a4e0%252D82d7%252D1547274208%2526bppcataid%253D0%2526vvid%253DC994087D%252DC02C%252D4302%252DA015%252D2954DB4AE354%2526appid%253Dcom%252Epptv%252Eiphoneapp%2526appplt%253Diph%2526appver%253D7%252E7%252E5&H=%E3%80%8A%E5%B0%8F%E5%A5%B3%E8%8A%B1%E4%B8%8D%E5%BC%83%E3%80%8B%E4%B8%8D%E5%BC%83%E5%88%B7%E7%94%9F%E5%AD%98%E5%89%AF%E6%9C%AC%EF%BC%8C%E5%BE%92%E6%89%8B%E6%8A%93%E8%80%81%E9%BC%A0%E6%AC%B2%E7%94%9F%E5%90%83&DM=2&utm&I=5570&J=796ababc8170b8c10f463ff0383c6a88.mp4&D5&PD=1.1.1.11309&K&L=954&Tab&M=0&F1=1&N=0&W1&PF&O=0&W2&P=0&Q=0&_CATAID1'
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


#print len(param_dict),len(ext_dict)
