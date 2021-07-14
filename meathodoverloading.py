#when a same is used but different para meters are passed
class mathamatics:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        s=1
    def average(self,a,b,c):
        if a!=None and b!=None and c!=None:
            s=(a+b+c)/3
        elif a!=None and b!=None:
            s=(a+b)/2
        elif a!=None:
            s=a
        print (s)

m1=mathamatics(20,30,40)
m1.average(10,30,50)

#print(s)
