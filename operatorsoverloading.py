class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return(s3)

    def __mul__(self,other):
        m1=(self.m1*other.m1)/2
        m2=(self.m2*other.m2)/2
        s3=student(m1,m2)
        return s3


s1=student(90,89)
s2=student(91,88)

#s3=s1+s2
s3=s1*s2
print(s3.m1,s3.m2)
