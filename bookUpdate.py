#encoding=utf-8
import requests
import json
from lxml import etree
import time
import random
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
qd_book_dic={'3621897':None,'2494758':None,'1004608738':None}
zh_book_id={'408586':None,'685640':None}
book_name={'3621897':'真武世界','2494758':'武炼巅峰','1004608738':'圣墟','408586':'逆天邪神','685640':'元尊'}
book_list=[qd_book_dic,zh_book_id]
USER_AGENT = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
            
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
            ]


def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def get_qd_info(bookID):
    
    headers={
            'Host': 'book.qidian.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': USER_AGENT[random.randint(0,12)],
            'Referer': 'https://book.qidian.com/info/%s' %(bookID),
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',

             }
    response=requests.get('https://book.qidian.com/info/1004608738',headers=headers)
    csrfToken = response.cookies.get_dict()['_csrfToken']
    cataUrl='https://book.qidian.com/ajax/book/category?_csrfToken=%s&bookId=%s' %(csrfToken,bookID)
    response=requests.get(cataUrl)
    rspJson=json.loads(response.content)
    cataList=rspJson['data']['vs'][-1]['cs']
    title=cataList[-1]['cN']
    if(qd_book_dic[bookID]==None):
        print 'init book %s' %(book_name[bookID])
        qd_book_dic[bookID]=title
    elif qd_book_dic[bookID]!=title:
        qd_book_dic[bookID]=title    
        send(book_name[bookID],title)



    
def get_zh_info(bookID):
    headers={
            'Host': 'book.zongheng.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': USER_AGENT[random.randint(0,12)],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'ZHID=B353AC9FB71C01A1844B842337A3624D; platform=H5; PassportCaptchaId=83b6d87f0df926aa50bd55025ae09e63; AST=15396686354379e83bf3d31; ver=2018; zh_visitTime=1539661427512; zhffr=0; UM_distinctid=1667af8f343ec4-07c7ebbfac1b2a-333b5602-1fa400-1667af8f344a0c; CNZZDATA30037065=cnzz_eid%3D1696240448-1539657443-%26ntime%3D1539657443; Hm_lvt_c202865d524849216eea846069349eb9=1539661428; v_user=%7Chttp%3A%2F%2Fbook.zongheng.com%2Fshowchapter%2F408586.html%7C24315083; JSESSIONID=abcJ6ajJvllR-4KzP_6zw; rSet=1_3_1_14; Hm_lpvt_c202865d524849216eea846069349eb9=1539661527',

             }
    zh_url='http://book.zongheng.com/showchapter/%s.html' %(bookID)
    response = requests.get(zh_url,headers=headers)
    resp_html=etree.HTML(response.content)
    #print response.content
    cataList=resp_html.xpath('.//li[@class="vip col-4"]')
    title=cataList[-1].xpath('./a/text()')[0] 
    if(zh_book_id[bookID]==None):
        print 'init book %s' %(book_name[bookID])
        zh_book_id[bookID]=title
    elif(zh_book_id[bookID])!=title:
        zh_book_id[bookID]=title
        send(book_name[bookID],title)
       
def send(name,title):
    from_addr='463664860@qq.com'
    password='dnxmdmmzfmnjbhcf'
    to_addr='790794090@qq.com'
    smtp_server='smtp.qq.com'
    msg=MIMEText('%s:%s' %(name,title),'plain','utf-8')
    msg['From']=_format_addr('更新提醒<%s>' %from_addr)
    msg['TO']=_format_addr('QQ邮箱<%s>' %to_addr)
    msg['Subject']=Header('%s更新啦' %(name),'utf-8').encode()
    server=smtplib.SMTP(smtp_server,25)
    server.login(from_addr, password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()

def send_mail(booklist):
    while 1:
        try:
            for bookID in booklist[0].keys():
                get_qd_info(bookID)
                s=random.randint(1,3)
                print book_name[bookID]
                print booklist[0][bookID]
                time.sleep(s)
            
            for bookID in booklist[1].keys():
                get_zh_info(bookID)
                s=random.randint(1,3)
                print book_name[bookID]
                print booklist[1][bookID]
                time.sleep(s)
        except Exception as e:
            print e
        time.sleep(60)

def get_page_num(proxy_url):
    headers={
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'User-Agent': USER_AGENT[random.randint(0,12)],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
             }

    response=requests.get(proxy_url,headers=headers)
    proxy_html=etree.HTML(response.content)
    page_num=int(proxy_html.xpath(".//div[@class='pagination']/a/text()")[-2])
    return page_num

def parse_ip_port(proxy_url):
    headers={
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'User-Agent': USER_AGENT[random.randint(0,12)],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
             }

    
    response=requests.get(proxy_url,headers=headers)
    proxy_html=etree.HTML(response.content)
    tr_list=proxy_html.xpath(".//table[@id='ip_list']/tr")
    for tr in tr_list:
        td_list=tr.xpath(".//td/text()")
        if td_list:
            ip=td_list[0]
            port=td_list[1]
            print ip,':',port

def get_proxy():
    init_url='http://www.xicidaili.com/wn/1'
    page_num=get_page_num(init_url)
    for i in range(1,page_num+1):
        proxy_url='http://www.xicidaili.com/wn/%d' %(i)
        parse_ip_port(proxy_url)

if __name__=='__main__':
    #send('ggg','hhhh')
    #get_proxy()
    send_mail(book_list)
