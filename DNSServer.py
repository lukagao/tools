#encoding=utf-8
import socket
from threading import Thread
import sys
import re
from _ast import Raise

class DNSServer(object):
    
    
    
    def __init__(self):
        self.host_ip_map = {}
        self.udps=None
        hostsfile = None
        if len(sys.argv) >= 1:
            if len(sys.argv) > 2 or sys.argv[-1] == '-h' or sys.argv[-1] == '--help':
                self.usage()
            else:
                hostsfile = 'hosts'
                self.host_ip_map = self.get_host_ip_map(hostsfile)
        print 'SimpleDNSServer :: hosts file -> %s\n' % hostsfile
        
        try:
            self.udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udps.bind(('',53))
        except Exception, e:
            print "Failed to create socket on UDP port 53:", e
            sys.exit(1)
        
        
            
    
    def get_domain(self,querymsg):
        
        domain=b''
        opcode=(ord(querymsg[2])>>3)&15 #0表示标准查询，1表示反向查询，2表示服务器状态请求
        if opcode==0:
            pos=12
            length=ord(querymsg[pos])
            while length != 0:
                domain+=querymsg[pos+1:pos+1+length]+'.'
                pos+=length+1
                length=ord(querymsg[pos])
        return domain
    
    def answer(self,ip,message):
        packet=b''
        packet+=message[:2]+'\x81\x80'
        packet+=message[4:6]+message[4:6]+'\x00\x00\x00\x00'
        packet+=message[12:]
        packet+='\xc0\x0c'
        packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'
        packet+=str.join('',map(lambda x:chr(int(x)),ip.split('.')))
        return packet
    # get_ip_address by domain name
    def get_ip_address_by_domain(self,domain):
        ip_address = '127.0.0.1'
        domain = domain.rstrip('.')
        if self.host_ip_map.has_key(domain):
            ip_address = self.host_ip_map[domain]
        else:
            list = socket.getaddrinfo(domain, 80)
        #print list
            if len(list) > 0:
                ip_address = list[0][4][0]
            
        return ip_address

    def get_host_ip_map(self,hostsfile):
        host_ip_map = {}
        try:
            f = open(hostsfile)
            for l in f.readlines():
                if not l.startswith('#'):
                    addrs = re.findall('[^\s]+', l)
                    if len(addrs) > 1:
                        for ad in addrs[1:]:
                            host_ip_map[ad] = addrs[0]
        except:
            pass
        finally:
            if f:
                f.close()
    
        return host_ip_map


    def query_and_send_back_ip(self,data,addr):
        domain=self.get_domain(data)
        if domain:
            try:
                print '-----------------------------------------------------------------------'
                print "Query info:"
                print 'Request domain: %s' % domain
                print 'Client addr and port:', addr
                ip = self.get_ip_address_by_domain(domain)
                if(ip):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.sendto(self.answer(ip,data), addr)
                    print 'IP for domain Request: %s -> %s' % (domain, self.get_ip_address_by_domain(domain))
                    sock.close()
            except Exception, e:
                print 'query for:%s error:%s' % (domain, e)
            
    def startServer(self):           
             
        try:
            while 1:
                data, addr = self.udps.recvfrom(1024)
                if data and addr:
                    t=Thread(target=self.query_and_send_back_ip,args=(data,addr))
                    t.start()
                #thread.start_new_thread(query_and_send_back_ip, (data, addr))
        except KeyboardInterrupt:
            print '\n^C, Exit!'
        except Exception, e:
            print '\nError: %s' % e
        finally:
            self.udps.close()


    def usage(self):
        print ""
        print "Usage:"
        print "" 
        print "\t# SimpleDNSServer [hosts file]"
        print ""
        print "Description:"
        print ""
        print "\tSimpleDNSServer will redirect DNS query to local machine."
        print ""
        print "\tYou can optionally specify a hosts file to the command line:\n"
        print "\t\t# SimpleDNSServer hosts\n"
        print "\tThe ip address will be chosen prior to system hosts setting and remote dns query from local machine. \n"
        print "\tIf SimpleDNSServer and the DNS setting machine are same, you should set an optional DNS server in the DNS setting to avoid DNS query failure caused by redirecting recursively.\n"
        print ""
    
        sys.exit(1)
    


if __name__ == '__main__':
    server=DNSServer()
    server.startServer()
     
    
                