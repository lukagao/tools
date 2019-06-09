#encoding=utf-8
import socket
import time
import json
import os
import subprocess
import re

key_list=['ct','vdid','psts','pbc','pbt','cdnip','br','bwtp','chge','pgnt','ctp','ptp','dgbc','dgbt',
          'pdl','plid','channelname','categoryname','timestamp','watchmillisec','status','sectiontime',
          'pure_uid','ft','bwt','isp','decodemode','wifis','cate','bppcateid','bppcate',
          'subbppcateid','subbppcate','section_id','section_name','setid','setname','mr2','adrequest',
          'fad','adresponse','adresponsefail','fad1','adrequest2','adplay',
          'adplayfail','sdk_streaming_error_code','sdk_ppbox_error_code','sdk_peer_error_code','programShowConsuming',
          'adShowConsuming','playConsuming','Opver','ad_play','playre','playtype','OPerrorCode','mr3','mr4','mr5',
          'adresponse1','fad2','opcj','opunion','adrequest3'     
          ]

print len(key_list)
param='{"cdnip":"","plid":"95955188-7492-43C9-A860-19F7438CB2FF","sec":"1","pbt":"0","pdl":"1005","vdid":"29549639","bwtp":"0","ctp":"","dgbt":"0","psts":"1","pbc":"0","pgnt":"","ct":"20190112142833274","chge":"2","ext":{"categoryname":"","timestamp":"1547274513","adrequest3":"","setid":"","subbppcate":"","fad2":"","Opver":"0.2.17","playtype":"1","sectiontime":"","fad":"","adplay":"2","decodemode":"2","bwt":"0","ad_play":"1","adplayfail":"","isp":"","cate":"","sdknm":"oneplayer","cdnip":"","channelname":"《小女花不弃》不弃刷生存副本，徒手抓老鼠欲生吃","pure_uid":"7EF13E8A-273F-42C2-98A6-AC79FB4B5F8B","watchmillisec":"0","bppcate":"","OPerrorCode":"","status":"1","sdk_peer_error_code":"","adrequest2":"1","section_name":"","setname":"","sdk_streaming_error_code":"","mr2":"","sdk_ppbox_error_code":"","adShowConsuming":"0","mr3":"","adresponse":"0","opunion":"com.pptv.iphoneapp","opcj":"detail.pptv|small.pptv|detail.sportsdk|other.sportsdk","wifis":"","bppcateid":"","subbppcateid":"","adresponse1":"","adresponsefail":"","mr4":"","playre":"","fad1":"0","ft":"2","playConsuming":"0","adrequest":"2","section_id":"","programShowConsuming":"0","mr5":""},"ptp":"2","viewtp":"native","dgbc":"0","br":"1759"}'
param_dict=json.loads(param)
ext_dict=param_dict['ext']
for item in key_list:
    if param_dict.has_key(item)==False and ext_dict.has_key(item)==False:
        print item
print 'external-------------------------------------------'

for item in param_dict.keys():
    if item not in key_list:
        print item
for item in ext_dict.keys():
    if item not in key_list:
        print item
#print len(param_dict),len(ext_dict)
