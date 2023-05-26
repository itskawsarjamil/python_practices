numbers= [10,20,10,40,30,60,70]
target=50



class Find_pair:
    def __init__(self,numbers,target):
        self.numbers=numbers
        self.target=target
    
    def pair(self):
        
        numbers2=set()
        list1=list()
        
        for i,num in enumerate(self.numbers):
            if num not in numbers2:
                numbers2.add(num)
            elif num in numbers2:
                continue

            j=i+1
            while j<len(self.numbers):
                num2=self.numbers[j]
                if num+num2==target:
                    # print(f'({num} {i+1},{num2} {j+1})')
                    list1.append((i+1,j+1))
                j=j+1
                
        return list1

my_pair=Find_pair(numbers,target)
print(my_pair.pair())


