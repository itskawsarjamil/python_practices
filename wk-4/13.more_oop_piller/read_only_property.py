class Student:
    def __init__(self,name,id,marks):
        self._name=name
        self.__id=id
        self.marks=marks
    
    @property    
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        del self._name
    
    @property
    def get_id(self):
        return self.__id
    

chowdhuri=Student('ab chowdhuri','200','100')

print(chowdhuri.name)
print(chowdhuri.get_id)
chowdhuri._Student__id=100
print(chowdhuri.get_id)
del chowdhuri.name
print(chowdhuri.__dict__)
