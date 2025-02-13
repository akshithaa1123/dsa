class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    capacity=5
    top=0
    def __init__(self):
        self.Head=None
    def Push(self,data):
        newnode=Node(data)
        if self.top<self.capacity:
            print(newnode.data."is pushed into stack")
            newnode.next=self.Head
            self.Head=newnode
            self.top+=1
        else:
             print("stack overflow") 
    def Pop(self):
        if self.top>0:
            print(self.Head.data,"is popped from the stack")
            self.Head=self.Head.next
            self.top-=1
        else:
            print("stack underflow")
    def Peek(self):
        if self.top>0:
            print(self.Head.data,"is top element in stack")
        else:
            print("stack is empty")    
    def Display(self):
        if self.top<0:
            print("stack is empty")
        else:
            print("stack:",end=" ")
            temp=self.Head            
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
                print()

if __name__=="__main__":
    stk=Stack


           