

class User:
    def __init__(self,name,roll,password):
        self.name=name
        self.roll=roll
        self.password=password
        self.borrow_books=[]
        self.returned_books=[]

class Library:
    def __init__(self,book_list):
        self.book_list=book_list
        
    def borrow_books(self,book_name,user):
        book_name=book_name.lower()
        for book in self.book_list:
            if book==book_name:
                for bk in user.borrow_books:
                    if book_name==bk:
                        print("age ferot de")
                        return
                
                if self.book_list[book]>0:
                    user.borrow_books.append(book)
                    self.book_list[book]-=1
                    return
                else:
                    print("book is not available")
                    return
            else:
                print("This type of any book is not exist in my library")
                return
    
    def returned_book(self,bookName,currentUser):
        for book in self.book_list:
            if book == bookName:
                for bk in currentUser.borrow_books:
                    if bk==book:
                        self.book_list[bookName]+=1
                        currentUser.borrow_books.remove[bookName]
                        currentUser.returned_books.appened(bookName)
                        return
                    else:
                        print("age ne pore dis")
                        return
            else:
                print("ei boi amar na.kar te anso")
                return
                
    
                
        
library=Library({"english":0,"bangla":3,"Math":4})
allUsers=[]
currentUser=None

while True:
    if currentUser==None:
        print("Not logged in\nPlease Login or create account(L/C)")
        option=input()
        match=False
        if option=="L":
            roll=int(input("Roll: "))
            password=input("Password: ")
            for user in allUsers:
                if user.roll==roll and user.password==password:
                    print("User found")
                    currentUser=user
                    match=True
                else:
                    print("User not found")
                    # break
        else:
            name=input("Name: ")
            roll=int(input("Roll: "))
            password=input("Password: ")
            currentUser=User(name,roll,password)
            
    
    else:
        print("Options")
        print("___________")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Borrowed books list")
        print("4. Returned books list")
        print("5. Check availability")
        print("6. Donate")
        print("7. Logout")
        x=int(input("Give option: "))
        if x==1:
            bookName=input("Book name: ")
            library.borrow_books(bookName,currentUser)
        elif x==2:
            bookName=input("Book name: ")
            library.return_book(bookName,currentUser)
        elif x==3:
            print(currentUser.borrow_books)
        elif x==4:
            print(currentUser.returned_book)
        elif x==5:
            for book in library.book_list:
                print(book)
        elif x==6:
            pass
        elif x==7:
            currentUser=None
            match=False    
        print("\n\n\n")    
            
                