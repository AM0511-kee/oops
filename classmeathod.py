#static,class,instance meathod

class student:
    school='rpc matric hr sec sch'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avr (self):
        average=(self.m1+self.m2+self.m3)//3
        return average


    @classmethod
    def scl_name(cls):
        return(cls.school)

    @staticmethod
    def printit():
        print('we educate people')

stu1=student(80,76,67)
stu2=student(90,83,43)
student.school='donbas school'
student.printit()
print(stu1.avr())
print(stu1.school)
