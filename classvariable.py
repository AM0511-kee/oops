#varible:class variable, meathod variable


class bikes:
    tyres=2
    tyres_type='heavy'

    def __init__(self,company,model_type,milage,riders):
        self.company=company
        self.model_type=model_type
        self.milage=milage
        self.riders=riders



bikes.tyres_type ='medium'

a=bikes('yamaha','R1M','5-10','Valentino rossi')
b=bikes('Honda','rc213v','5-10','marc marques')

print(a.company,a.model_type,a.milage,a.riders,a.tyres_type)
