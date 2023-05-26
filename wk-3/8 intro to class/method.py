class Phone:
    color='black'
    features=['camera','water proof','can be used as a hammer']
    def call(self):
        print("ring ring ring")
    
    def send_sms(self,number,text):
        sms=f'sending sms: {text} to: {number}'
        return sms
    
my_phone=Phone()

my_phone.call()

print(my_phone.send_sms(234234232,'I missed to miss you'))