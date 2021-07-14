#creating an object(oops)
class computer:
    def __init__(self,processor,ram,graphics):
        self.processor=processor
        self.ram=ram
        self.graphics=graphics

    def update(self,ram):
        self.ram = ram


    def config(self):
        print('configuration is : '  ,self.processor,self.ram,self.graphics)

    def compare(self,other):
        if self.processor == other.processor:
            return True
        return False



c1=computer('amd','8gb','razen5')
c2=computer('intel i5','8gb','nvidi')
c3=computer('intel i7','16gb','intel')

c3.update('12gb')
c1.config()
c2.config()
c3.config()
if c2.compare(c3):
    print('there have same processor....')

print('they have different processor....')
