class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    front=-1
    rear=-1
    def __init__(self):
        self.front=None
        self.rear=None
    def Enqueue(self,data):
        newnode=Node(data)
        if self.front==None and self.rear==None:
            print(newnode.data,"is enqueued into queue")
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode 
            print(newnode.data,"is enqueued into queue")
    def Dequeue(self):
        if self.front==None and self.rear==None:
            print("Queue is empty")
        elif self.front==self.rear:
            print(self.front.data,"is dequeued from the queue")
            self.front=None
            self.rear=None
        else:
            print(self.front.data,"is dequeued from the queue")
            self.front=self.front.next
    def Peek(self):
        if self.rear!=None:
            print(self.rear.data,"is last element in Queue")
        else:
            print("Queue is empty")    
    def Display(self):
        if self.front==None:
            print("Queue is empty")
        else:
            print("Queue:",end=" ")
            temp=self.front            
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print()

if __name__=="__main__":
    q=Queue()
    front=-1
    rear=-1
    print("welcome to Queue operations")

    print("enter 1 to Enqueue an element into Queue")
    print("enter 2 to Dequeue an element into queue")
    print("enter 3 to show PEEK of the Queue")
    print("enter 4 to DISPLAY elements of Queue")
    print("enter -1 to EXIT from Queue\n")
    while True:
        ip=int(input("enter your choice:"))
        if ip==1:
            data=int(input("enter the value to be pushed into Queue:"))
            q.Enqueue(data)
        elif ip==2:
            q.Dequeue()
        elif ip==3:
            q.Peek()
        elif ip==4:
            q.Display()
        elif ip==-1:
            print("you have been exited form the Queue")
            break
        else:
            print("ivalid input")
