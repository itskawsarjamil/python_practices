class User:
    def __init__(self,name,password,phone):
        self.name=name
        self.__password=password
        self.__phone=phone
    
    def __get_password(self):
        print(self.__password)
    
    
    def user_login(self,name,password):
        if(name==self.name and password==self.__password):
            return True
        return False
    
my_user=User('Kawsar','12345678','16514465465')
# print(my_user.__password)
print(my_user.name)
# print(my_user.__get_password())
print(my_user.user_login('Kawsar','12345678'))