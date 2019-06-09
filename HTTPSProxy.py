#encoding=utf-8
#import socket
from threading import Thread
import re
import myssl
import _socket
import requests

    
def start_proxy(conn,addr):
    
    #print 'start thread'
    proxies={
                'http':'http://127.0.0.1:8888'
            }
    client_header=''
    while 1:
        buf = conn.recv(2048)
        client_header += buf
        if len(buf) < 2048:
            break
    
    #and 'api.ddp.vip.pptv.com' in client_header
    if 'CONNECT' in client_header and 'isports.suning.com' in client_header:

        
        host_pattern=re.compile(r'CONNECT(.+):')
        port_pattern=re.compile(r':(.+)HTTP')
        host=host_pattern.findall(client_header)[0].strip()
        port=port_pattern.findall(client_header)[0].strip()
        print '--------------------------------------------------------------------------'
        #print host
        #print port
        print client_header
        conn.sendall(bytes('HTTP/1.1 200 Connection Established\r\n\r\n'))  
        '''
        ctx=_ssl._SSLContext(2)
        ctx.load_cert_chain(certfile='sn_new_server.crt',keyfile='sn_new_server_key.pem')
        ssl=ctx._wrap_socket(conn,1)
        print ssl.do_handshake()
        print ssl
        
        '''
        ctx=myssl.SSLContext()
        ctx.load_certificate('sn_new_server.cer','sn_new_server_key.pem',myssl.PySSL_FILETYPE_ASN1,myssl.PySSL_FILETYPE_PEM)
        ssl=ctx.Create_SSLSocket(conn,myssl.SSL_Server_Method)
        ssl.SSL_do_handshake()
        ssl.SSL_recv(0)
        count=ssl.SSL_pending()
        reqMsg=ssl.SSL_recv(count)
        print 'request message:'
        print reqMsg
     
        toserver_socket=_socket.socket(_socket.AF_INET,_socket.SOCK_STREAM)
        toserver_socket.connect((host,int(port)))
        to_server_ctx=myssl.SSLContext()
        to_server_ssl=to_server_ctx.Create_SSLSocket(toserver_socket,myssl.SSL_Client_Method)
        to_server_ssl.SSL_do_handshake()
        to_server_ssl.SSL_send(reqMsg)
        to_server_ssl.SSL_recv(0)
        count=to_server_ssl.SSL_pending()
        rspMsg=to_server_ssl.SSL_recv(count)
        print 'response message:'
        print rspMsg
        '''
        rspMsg=to_server_ssl.SSL_recv(200000)
        print 'chunked message:'
        print rspMsg
        '''
        ssl.SSL_send(rspMsg)
        conn.close()
        
    conn.close()
    
    


if __name__ == '__main__':
    s=_socket.socket()
    s.setsockopt(_socket.SOL_SOCKET, _socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0',8080))
    s.listen(1500)
    while 1:
        conn,addr=s.accept()
        #print addr
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
        