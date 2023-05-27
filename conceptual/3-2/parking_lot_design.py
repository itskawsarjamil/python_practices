class Car:
    def __init__(self,license,model,color):
        self.license=license
        self.model=model
        self.color=color
    
class Garage:
    def __init__(self):
        self.car_added=[]
        self.slot=10
        self.car_infos={}
        self.ticket=[]
        self.bill=0
        