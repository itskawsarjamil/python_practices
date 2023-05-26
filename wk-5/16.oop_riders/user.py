import hashlib
from brta import BRTA

license_authority=BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        
        pwd_hashed=hashlib.md5(password.encode()).hexdigest()
        self.password=pwd_hashed
        
        with open('user.txt','w') as file:
            file.write(f'{email} {pwd_hashed} \n')
        file.close()
        print(self.name,'user created')
        
    @staticmethod    
    def log_in(email,password):
        user_pass_hashed=hashlib.md5(password.encode()).hexdigest()
        # print(user_pass_hashed)
        with open('user.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                # print(line)
                if email in line:
                    
                    stored_hash_pass=line.split(' ')[1]
                    
                    # print(stored_hash_pass)
                    
                    if user_pass_hashed==stored_hash_pass:
                        print('valid user')
                        return
                    else:
                        print('Incorrect Password')
                        return
                else:
                    print('give correct mail')
                    return
        
class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location=location
        self.balance=balance
        super().__init__(name, email, password)
    
    def set_location(self,location):
        self.location=location
        
    def get_location(self):
        return self.location
    
    def request_trip(self,destination):
        pass
    
    def start_a_trip(self,fare):
        self.balanc-=fare
        
class Driver(User):
    def __init__(self, name, email, password,location,license=None) -> None:
        self.location=location
        self.license=license
        self.valid_driver=license_authority.validate_license(email,license)
        self.earning=0
        super().__init__(name, email, password)   
    
    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result ==False:
            print('sorry you failed,try again')
        else:
            self.license=result
            self.valid_driver=True
        
    def start_a_trip(self,destination,fare):
        self.location=destination
        self.earning+=fare    
        
             
user1=User('ABC','abc@def.com','123456')
# user2=User('def','def@ghi.com','asdfhkl')

User.log_in('abc@def.com','123456')

kuber=Driver('kuber','kuber@maji.com','kuberjaisna','padda','345')
result=license_authority.validate_license(kuber.email,kuber.license)
print(result)
kuber.take_driving_test()

result=license_authority.validate_license(kuber.email,kuber.license)

print(result)