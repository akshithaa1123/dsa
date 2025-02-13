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
    def DeleteAtEnd(self):
        if self.Head==None:
            print("no data exist to delete")
        elif self.Head.next==None:
            self.Head=None
        else:
            temp=self.Head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def DeleteAtBegin(self):
        if self.Head==None:
            print("no data exist to delete")
        elif self.Head.next==None:
            self.Head=None
        else:
            self.Head=self.Head.next
    def DeleteAtPosition(self,pos):
        if(pos==1):
            self.Head=self.Head.next
        else:
            temp=self.Head
            while(pos-2):
                temp=temp.next
                pos-=1
            temp.next=temp.next.next    

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
sll.Display();print()
sll.InsertAtBegin(0)
sll.InsertAtBegin(-1)
sll.Display();print()
sll.InsertAtMiddle(3,6)
sll.Display();print()
sll.DeleteAtEnd()
sll.Display();print()
sll.DeleteAtBegin()
sll.Display();print()
sll.DeleteAtPosition(3)
sll.Display()