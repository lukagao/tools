#!/usr/bin/env python
# coding=utf-8
import base64
import sys
import urlparse
import urllib

#PASSWORD = 'pplive' # 普通统计
#PASSWORD = 'pp%sdk(sdk)' # 统计SDK
#PASSWORD = '%@&#$EOQWIU31!DA421' #在线统计
PASSWORD = ''
def decode(s):
    data = base64.decodestring(s)

    if not PASSWORD:
        return data

    bytes = bytearray(len(data))
    for i in range(0, len(bytes)):
        byte = ord(data[i]) - ord(PASSWORD[i % len(PASSWORD)])
        bytes[i] = chr(byte if byte > 0 else byte + 255)

    return str(bytes)

if __name__ == '__main__':
    result = decode(raw_input("input string"))
    print result
    print '\n'

    semi_idx = result.find(';')

    acts = []
    if semi_idx > 0:
        acts.extend(result[semi_idx + 1:].split(';'))
    parse = urlparse.parse_qsl(result)

    k_v = []
    for k, v in parse:
        if k == 'act':
            acts.insert(0, v)
        else:
            k_v.append((k, v))

    k_v.sort()
    for k, v in k_v:
        print k+":\t", v
        
        

    '''
    for idx, act in enumerate(acts):
        if not act:
            continue
        print 'act %s:' % idx
        for comp in act.split(','):
            colon_idx = comp.find(':')
            if colon_idx != -1:
                print ' ', comp[:colon_idx], ':', urllib.unquote(comp[colon_idx + 1:])
            else:
                print ' ', comp
    '''