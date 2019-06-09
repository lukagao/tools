#encoding=utf-8
import socket
import time
import json
import os
import subprocess
import re

key_list=[
          'psr','pt','isps','psts','ct','tknid','pgnt','pbc','pbt','br','adls','pdl','pte','vdid','chge','dgc','dgbt',
          'ctp','ptp','plid','cdnip','detailcost','MP4FileName', 'playmode','bwtype','sdkversion','sdkruning','Tab',
          'playmode2','playertype','PlayStopReason','playprotocol','PlayForm','ThirdSource','TVSection','mobileOrderFetch',
          'DRseq','ChannelChineseName','pvid','decodemode','recstats','timedetail','detailready','errorcode',
          'videoSecond','playerVersion','timeall','channelType','sectionid','seriesid','baikeid','vdnm','cate','bppcateid',
          'bppcate','subbppcateid','subbppcate','aotunavi','BitrateBufferTime','lianbo','playfailureduration','setid','setname',  
          'mr2','adrequest','fad','adresponse','adresponsefail','fad1','adrequest2','adplay',
          'adplayfail','sdk_streaming_error_code','sdk_ppbox_error_code','sdk_peer_error_code','programShowConsuming',
          'adShowConsuming','playConsuming','Opver','ad_play','playre','playtype','OPerrorCode','mr3','mr4','mr5',
          'adresponse1','fad2','opcj','opunion','adrequest3'     
          ]

print len(key_list)
param='{"pgnt":"","psts":"1","dgc":"0","ptp":"2","psr":"","vdid":"29549639","viewtp":"native","ext":{"baikeid":"","fad1":"0","MP4FileName":"796ababc8170b8c10f463ff0383c6a88.mp4","sdk_streaming_error_code":"","playertype":"0","mr2":"","timedetail":"","sdk_ppbox_error_code":"","detailcost":"","bwtype":"0","adplay":"2","mr3":"","Opver":"0.2.17","ThirdSource":"","playerVersion":"2.1.6","sdkversion":"1.1.1.11309","BitrateBufferTime":"0","aotunavi":"","playmode":"2","ChannelChineseName":"《小女花不弃》不弃刷生存副本，徒手抓老鼠欲生吃","mr4":"","fad2":"","opunion":"com.pptv.iphoneapp","mr5":"","TVSection":"","pvid":"","recstats":"","playprotocol":"2","ad_play":"1","adrequest2":"1","adrequest3":"","setname":"","adresponse":"0","adplayfail":"","videoSecond":"92000","adShowConsuming":"0","setid":"","fad":"","vdnm":"《小女花不弃》不弃刷生存副本，徒手抓老鼠欲生吃","errorcode":"","timeall":"","bppcateid":"","sdkruning":"1","cate":"","adrequest":"2","programShowConsuming":"0","adresponse1":"","sectionid":"","playtype":"1","seriesid":"0","playConsuming":"0","sdknm":"oneplayer","channelType":"1","playfailureduration":"","PlayStopReason":"","playre":"","lianbo":"","cdnip":"","decodemode":"2","opcj":"detail.pptv|small.pptv|detail.sportsdk|other.sportsdk","subbppcate":"","subbppcateid":"","PlayForm":"","Tab":"","DRseq":"2","playmode2":"0","bppcate":"","adresponsefail":"","OPerrorCode":"","detailready":"","mobileOrderFetch":"","sdk_peer_error_code":""},"plid":"95955188-7492-43C9-A860-19F7438CB2FF","pbt":"0","ct":"20190112142833274","pdl":"1005","pte":"0","isps":"1","chge":"2","sec":"1","pbc":"0","ctp":"","dgbt":"0","adls":"0","um":"2","br":"1759","pt":"0","tknid":""}'
param_dict=json.loads(param)
ext_dict=param_dict['ext']
print '少发--------------------------------------------------'
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
