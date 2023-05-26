class Person:
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.money=money
    def __add__(self,other):
        return self.age+other.age
    def __call__(self):
        print(f"This is {self.name} with age {self.age} with money {self.money}")
    def __eq__(self,other):
        return self.age==other.age

my_person=Person('kawsar',23,19)
my_person2=Person('Jamil',20,9)

print(my_person+my_person2)
print(my_person==my_person2)
my_person()