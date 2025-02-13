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
    def InsertAtBegin(self,data):
        newnode=Node(data)
        if self.Head==None:
            self.Head=newnode
        else:
            newnode.next=self.Head
            self.Head=newnode
    def InsertAtMiddle(self,pos,data):
        newnode=Node(data)
        temp=self.Head
        while(pos-1!=0):
            temp=temp.next
            pos-=1
        newnode.next=temp.next
        temp.next=newnode
            
    def Display(self):
        temp=self.Head            
        while(temp!=None):
            print(hash(temp),temp.data,hash(temp.next))
            temp=temp.next
sll=SinglyLinkedList()
sll.InsertAtEnd(1)
sll.InsertAtEnd(2)
sll.InsertAtEnd(3)
sll.InsertAtEnd(4)
sll.InsertAtBegin(0)
sll.InsertAtBegin(-1)
sll.InsertAtMiddle(3,6)
sll.Display()