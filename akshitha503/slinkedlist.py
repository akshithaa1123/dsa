class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.Head=None
    def InsertAtEnd(self,data):
        newnode=Node(data)
        if self.Head==None:
            self.Head=newnode
        else:
            temp=self.Head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def Display(self):
        temp=self.Head            
        while(temp!=None):
            print(temp,temp.data,temp.next)
            temp=temp.next
sll=SinglyLinkedList()
sll.InsertAtEnd(1)
sll.InsertAtEnd(2)
sll.InsertAtEnd(3)
sll.InsertAtEnd(4)
sll.Display()