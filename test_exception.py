#encoding=utf-8

class A(object):
    a=1
    def __init__(self,a):
        self.a=a
    
    def print_func(self):
        print self.a

class B(A):
    def __init__(self,b):
        A.__init__(self,b)

class C(A):
    def __init__(self):
        pass
        
b=B(2)
b.print_func()
c=C()
c.print_func()