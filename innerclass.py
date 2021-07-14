#creating a class within a c;ass where the inner class is used only in outer class
class cars:
    def __init__(self,company,model,milage):
        self.company=company
        self.model=model
        self.milage=milage
        self.uth=self.under_the_hood

    def show (self):
        print(self.company,self.model,self.milage)

    class under_the_hood:

        def __init__(self,engine,brakes,transmission):
            self.engine=engine
            self.brakes=brakes
            self.transmission=transmission
        def display(self):
            print('it works on {} with {} and {} transmission system'.format(self.engine,self.brakes,self.transmission))

#creating obeject of outer func
c1=cars('bmw','5series','6-10')
c2=cars('ford','mustang gtr','5-7')
#calling outer func
c1.show()
c2.show()
#creating objects of inner func by using object of outer func
spec1=c1.uth('v8','8 piston brakes','automatic')
spec2=c2.uth('v12','8 piston brakes','manual')
spec1.display()
spec2.display()
