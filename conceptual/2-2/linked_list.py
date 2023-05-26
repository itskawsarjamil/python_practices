
count = 0


class Node():
    def __init__(self, v):
        # print("Hello from Node")
        self.val = v
        self.next = None
        global count
        count = count+1


class Linked_List():
    def __init__(self):
        self.head = None

    def insert_at_pos(self, val, pos):
        if pos > count:
            print("wrong position")
            return

        newNode = Node(val)
        if (pos == 0):
            newNode.next = self.head
            self.head = newNode
        else:
            tmp = self.head
            for i in range(pos-1):
                tmp = tmp.next

                # by this we can also handle error without global variable
                if tmp == None:
                    print("Out of bound")
                    return

            newNode.next = tmp.next
            tmp.next = newNode

    def insert_at_tail(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            tempNode = self.head
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = newNode

    def delete_at_pos(self, pos):
        global count
        
        # print(count)
        if pos>=count:
            print("wrong position for delete")
            return
        count=count-1
        
        tmp = self.head
        if pos == 0:
            delNode = self.head
            self.head = self.head.next
            del delNode
        else:

            for i in range(pos-1):
                # print(i, tmp.val)
                tmp = tmp.next
                if tmp == None:
                    print("wrong position")
                    return

            delNode = tmp.next
            if delNode.next==None:
                print('wrong position for delete')
                return
            
            tmp.next = delNode.next
            del delNode
            print("deleted")
            self.print_list()


    def reverse(self):
        if self.head.next==None:
            return self.head
        save=self.head
        self.head=self.head.next
        newNode=self.reverse()
        save.next.next=save
        save.next=None
        return newNode

    
    def print_list(self):
        tmp = self.head
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next


def main():
    lst = Linked_List()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    lst.insert_at_pos(40, 3)
    lst.insert_at_pos(50, 4)
    # lst.insert_at_pos(6,0)
    lst.print_list()
    # lst.delete_at_pos(4)
    print("after reverse")
    lst.head=lst.reverse()
    lst.print_list()
    
    # lst.delete_at_pos(4)
    # print("deleted")
    # lst.print_list()


main()
