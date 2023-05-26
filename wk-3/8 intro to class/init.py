class Phone:
    manufactured='china'
    
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
        
    def send_sms(self,number,text):
        sms=f'sending:{text} to {number}'
        return sms
    
    
my_phone=Phone('Realme',13000,'blue')
print(my_phone.brand,my_phone.manufactured,my_phone.color,my_phone.price)
dad_phone=Phone('Symphony',1000,'black')
print(dad_phone.brand,dad_phone.manufactured,dad_phone.color,dad_phone.price)