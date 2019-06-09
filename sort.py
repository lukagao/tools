#encoding=utf-8
import math
from queues import Queue
import time
import new
#阶乘
def factorial(n):
    if n==0:
        return 1
    if n>0:
        return n*factorial(n-1)

#print factorial(20)

#阶乘末尾几个0
def zeroCount(n):
    count_5=0
    count_2=0
    for i in range(1,n+1):
        print i
        if i%5==0:
            while i%5==0:
                count_5+=1
                i=i/5
        if i%2==0:
            while i%2==0:
                count_2+=1
                i=i/2
    return min(count_2,count_5)
#print zeroCount(20)

#26进制转化10进制
def cton(cstr):
    numList=[]
    for i in range(len(cstr)):
        num=ord(cstr[i])-ord('a')
        if num<0 or num>25:
            return None
        else:
            numList.append(num)
    return reduce(lambda x,y:x*26+y, numList)

#print cton('baa')


#求数组最大子数组
def getMax(numList):
    maxnum=numList[0]
    index=0
    for i in range(len(numList)):
        if numList[i]>maxnum:
            maxnum=numList[i]
            index=i
    return maxnum,index
        

def getMaxSub(numList):
    length=len(numList)
    head=0
    cur=0
    cursum=0
    maxnum,index=getMax(numList)
    maxsum=[maxnum,index,index]
    while True:
        if head<length and cur<length:
            #print cur
            cursum=cursum+numList[cur]
            if cursum>maxsum[0]:
                maxsum=[cursum,head,cur]
            if cursum<0:
                head=cur+1
                cur=head
                cursum=0
                continue
            cur=cur+1         
        else:
            break
    return numList[maxsum[1]:maxsum[2]+1]
        
numList=[15,-6,3,2,7,-1,-2,-2]     
#print getMaxSub(numList) 
        
#求最大不重复子串
def getMaxStr(ostr):
    exist=[]
    length=len(ostr)
    head=0
    cur=0
    nowstr=''
    mstr=''
    maxstr=[0,0,0]
    
    while length-head>maxstr[0]:
        if head<length and cur <length:
            tmp=ostr[cur]
            if tmp not in exist:
                exist.append(tmp)
                nowstr+=tmp
                cur=cur+1
                if len(nowstr)>len(mstr):
                    mstr=nowstr
                continue
            else:
                head=head+1
                cur=head
                nowstr=''
                exist=[]
                
        else:
            break
    return mstr

ostr='abccdefg'
#print getMaxStr(ostr)
    
#两个字符串最大公共子串
def getCommonStr(fstr,sstr):
    flength=len(fstr)
    slength=len(sstr)
    maxstr=''
    for i in range(flength):
        for n in range(i,flength):
            if n-i+1<=slength:
                tmp=fstr[i:n]
                
                if tmp in sstr:
                    #print tmp
                    if len(tmp)>len(maxstr):
                        maxstr=tmp
    return maxstr

fstr='agdfsdd'
sstr='adgdfsdgh'
#print getCommonStr(fstr, sstr)

#print math.sqrt(6)   

#字符串所有重复的子串
def getDUPStr(lstr):
    child_map={}
    for length in range(2,len(lstr)):
        for head in range(len(lstr)-1):
            if head+length<=len(lstr):
                child=lstr[head:head+length]
                left=lstr[head+1:]
                if child in left:
                    if child_map.has_key(child):
                        num=child_map[child]+1
                    else:
                        num=1
                    child_map[child]=num
    return child_map

lstr='aaasdfgasdfghjasdf'
#print getDUPStr(lstr)

class Tree(object):
    left=None
    right=None
    value=0
    def __init__(self,value=None):
        self.value=value

t0=Tree(0)
t1=Tree(1)
t2=Tree(2)
t3=Tree(3)
t4=Tree(4)
t5=Tree(5)

t0.left=t1
t0.right=t2
t1.left=t3
t1.right=t4
t2.left=t5
flag=0
def firstTravel(t,level):
    if not t:
        return
    global flag
    if level>flag:
        flag=level
    print t.value
    firstTravel(t.left,level+1)
    firstTravel(t.right,level+1)
#firstTravel(t0,1)
#print 'deep:'+str(flag)

def middleTravel(t):
    if not t:
        return   
    middleTravel(t.left)
    print t.value
    middleTravel(t.right)         
          
#middleTravel(t0)       
        
def lastTravel(t):
    if not t:
        return   
    lastTravel(t.left)
    lastTravel(t.right)  
    print t.value
#lastTravel(t0)

def broadTravel(t):
    q=Queue()
    q.put(t)
    while q.qsize()>0:
        tmp=q.get()
        print tmp.value
        if tmp.left is not None:
            q.put(tmp.left)
        if tmp.right is not None:
            q.put(tmp.right)
#broadTravel(t0)

class LinkList(object):
    next=None
    value=None
    def __init__(self,value):
        self.value=value

l=LinkList(0)
l1=LinkList(1)
l2=LinkList(2)
l3=LinkList(3)
l.next=l1
l1.next=l2
l2.next=l3

def reverseLink(l):
    llist=[]
    llist.append(l)
    while l.next is not None:
        llist.append(l.next)
        l=l.next
    for i in range(1,len(llist)):
        llist[-i].next=llist[-i-1]
    llist[0].next=None
    return llist[-1]

def reverseLink1(l):
    newl=None
    nextl=None
    while l is not None:
        nextl=l.next
        l.next=newl
        newl=l
        l=nextl
    return newl
               
#lll=  reverseLink1(l)

#找出字符串最大回文字符串
def isHW(hstr):
    length=len(hstr)
    i=0
    j=length-1
    while i<=j:
        if hstr[i]==hstr[j]:
            i=i+1
            j=j-1
            continue
        else:
            return False
    return True

def getHW(hstr):
    length=len(hstr)
    hwList=[]
    for slen in range(2,length+1):    
        for head in range(length-1):
            if head+slen<=length:
                tmp=hstr[head:head+slen]
                if isHW(tmp):
                    hwList.append(tmp)
    return hwList

hstr='adada'
#print getHW(hstr)


#快速排序
def quickSort(numList,low,high):
    if low<high:
        middle=exchange(numList, low, high)
        print middle
        quickSort(numList, low, middle-1)
        quickSort(numList, middle+1, high)
    
def exchange(numList,low,high):
    middle=numList[low]
    while low<high:
        print low
        while low<high and numList[high]>=middle:
            high=high-1
        numList[low]=numList[high]
        while low<high and numList[low]<=middle:
            low=low+1
        numList[high]=numList[low]
    numList[low]=middle
    return low

numList=[0,1,6,7,3,2,4,9]
#quickSort(numList, 0, len(numList)-1) 
#print numList
#exchange(numList, 0, len(numList)-1) 


#堆排序
def heapAdjust(heap,low,high):
    tmp=heap[low]
    while low*2<=high:
        j=low*2
        if j<high and heap[j]<heap[j+1]:
            j=j+1
        if tmp>heap[j]:
            break
        heap[low]=heap[j]
        low=j
    heap[low]=tmp
    

def heapSort(heap):
    length=len(heap)-1
    middle=int(length/2)
    while middle>0:
        heapAdjust(heap, middle, length)
        middle=middle-1
    cur=length
    print heap
    while cur>1:
        #print cur
        tmp=heap[1]
        heap[1]=heap[cur]
        heap[cur]=tmp
        #print heap
        heapAdjust(heap, 1, cur-1)
        cur=cur-1
    
    
heap=[0,5,3,6,1,3,2,8]
#heapSort(heap)
#print heap

def binaryAdd(a,b):
    a=a&0xFFFFFFFF
    b=b&0xFFFFFFFF
    sum=a^b
    carry=(a&b)<<1
    while carry!=0:
        a=sum
        b=carry
        sum=a^b
        carry=(a&b)<<1
    md=sum%4294967296
    if md<2147483647:
        return md
    else:
        return md-4294967296   

#print binaryAdd(8, 2)

class StateMachine(object):

    anychar='00'
    index=0
    def __init__(self):
        self.current=[]
        self.next=[]
        self.next_ex=[]
        self.type=1
        self.index=StateMachine.index+1
        StateMachine.index=self.index

    def newState(self,p):
        p0=p[0]
        p1=None
        if len(p)>1:
            p1=p[1]
        if p0=='.':
            if p1 and p1=='*':
                self.type=2
                self.current.extend([None,self.anychar])
                self.next.append(self)
            else:
                self.current.append(self.anychar)
        else:
            if p1 and p1=='*':
                self.type=2
                self.current.extend([None,p0])
                self.next.append(self)
            else:
                self.current.append(p0)
        return self.type
    

def generateMC(p):
    machines=[]
    while True:
        mc=StateMachine()
        incre=mc.newState(p)
        machines.append(mc)
        p=p[incre:]
        if len(p)==0:
            break
    machine=machines[0]
    for i in range(1,len(machines)):
        print i
        machine.next.append(machines[i])
        machine.next_ex.append(machines[i])
        machine=machines[i]
    return machines[0]
class Solution: 
    def isMatch(self,s,p):
        if s==p:
            return True
        r=False
        index=0
        head=generateMC(p)
        machineMap={0:[head]}
        while True:
            newmap={}
            print machineMap
            for index in machineMap.keys():
                charc=s[index]
                for mc in machineMap[index]:
                    if charc in mc.current:
                        print charc+'匹配'
                        if newmap.has_key(index+1):
                            for m in mc.next:
                                if m not in newmap[index+1]:
                                    newmap[index+1].append(m)
                        else:
                            newl=[]
                            for item in mc.next:
                                newl.append(item)
                            newmap[index+1]=newl
                        r=True
                    elif ((charc>='a' and charc<='z') or (charc>='A' and charc<='Z')) and '00' in mc.current:
                        print '.匹配'
                        if newmap.has_key(index+1):
                            for m in mc.next:
                                if m not in newmap[index+1]:
                                    newmap[index+1].append(m)
                        else:
                            newl=[]
                            for item in mc.next:
                                newl.append(item)
                            newmap[index+1]=newl
                        r=True
                    if None in mc.current:
                        print "None迁移"
                        if newmap.has_key(index):
                            if mc.next_ex!=[]:
                                if mc.next_ex[0] not in newmap[index]:
                                    newmap[index].append(mc.next_ex[0])
                        else:
                            if mc.next_ex!=[]:
                                newmap[index]=[mc.next_ex[0]]
                        r=True


                    if len(s) in newmap.keys():
                        print "字符串结尾"
                        #time.sleep(5)
                        print mc.current,mc.index
                        #time.sleep(5)
                        while True:
                            #time.sleep(2)
                            if mc.next_ex==[]:
                                return r
                            mc=mc.next_ex[0]
                            #非*模式
                            if mc.type==1:
                                newmap.pop(len(s))
                                break
                    
            if r==False:
                print "无匹配"
                break
             
            machineMap=newmap
            r=False
        return r

#print Solution().isMatch('acaabbaccbbacaabbbb', 'a*.*b*.*a*aa*a*')
class FBSolution(object):
    def __init__(self):
        self.result={}
    def Fibonacci(self,n):
        if n==1 or n==2:
            return 1
        elif n==0:
            return 0
        elif n in self.result.keys():
            return self.result[n]
        else:
            res=self.Fibonacci(n-1)+self.Fibonacci(n-2)
            self.result[n]=res
            return res
fb=FBSolution()
print fb.Fibonacci(10)
    
