#encoding=utf-8
import socket
import requests
from threading import Thread
import re
from StringIO import StringIO

import zipfile
def start_proxy(conn,addr):
    
    print 'start thread'
    client_header=''
    proxies={
                'http':'http://127.0.0.1:8888'
            }
    headers = {}
    while 1:
        buf = conn.recv(2048)
        client_header += buf
        if len(buf) < 2048:
            break
    pattern = re.compile(r'\/zip([\s\S]+)--Boundary')
    data=pattern.findall(client_header)
    if data:
        print data[0]
        buf = StringIO(data[0])
        #f = gzip.GzipFile(fileobj=buf)
        f=zipfile.ZipFile(file=buf)
        for name in f.namelist():
            print f.read(name)
    #print client_header
    
    '''
    header_pattern=re.compile(r"(\S+):\s+(.+)")
    header_list = header_pattern.findall(client_header)
    for item in header_list:
        headers[item[0]]=item[1].encode().replace("\r","")

    print headers
    
    
    
    full_url='http://'
    path_pattern = re.compile(r"GET\s+(\S+)\s+HTTP\/")
    host_pattern=re.compile(r'Host:\s+(\S+(\.\S+)+)')
    path_list = path_pattern.findall(client_header)
    host_list = host_pattern.findall(client_header)
    if (host_list):
        full_url+=host_list[0][0]
        if(path_list):
            full_url+=path_list[0] 
            print full_url
        try:
            requests.get('http://127.0.0.1:8888')
        except Exception,e:
            proxies.pop('http')
            #print e
        resp=requests.get(full_url,proxies=proxies,headers=headers)
        headers=resp.headers
        response=b'HTTP/1.1 '
        code=str(resp.status_code)
        response+=code
        if (code=='200'):
            response+=' OK'+'\r\n'
        for key,value in headers.items():
            if key!='Transfer-Encoding' and key!='Content-Encoding':
                response+= key+': '+value+'\r\n'

        response+='\r\n'+resp.content
        print('send to', addr)
        conn.sendall(bytes(response))
    '''
    conn.close()


if __name__ == '__main__':
    s=socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0',80))
    s.listen(1500)
    while 1:
        conn,addr=s.accept()
        print addr
        t=Thread(target=start_proxy,args=(conn,addr))
        t.start()




#socket ��ʽ
        '''
        s1 = socket.socket()
        s1.connect(('pptv.com', 80))
        s1.sendall(headers.encode())
        resp = b''
        while 1:
            try:
                buf = s1.recv(1024*8)
            except socket.timeout as e:
                print(e)
                break
                
            resp += buf
            if not buf or\
               buf.startswith(b'WebSocket') and buf.endswith(b'\r\n\r\n'):
                break

        resp = resp.replace(b'Content-Encoding: gzip\r\n', b'')\
                   .replace(b't66y.com', b'bjgong.tk:1024')
        print resp
        '''
        