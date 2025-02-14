def Enqueue(data):
    global front
    global rear
    if front==-1 and rear==-1:
        queue.append(data)
        front=rear=0
        print(data,"is enqueued into queue")
    else:
        queue.append(data)
        rear+=1
        print(data,"is enqueued into queue")
        print(front,rear)
def Dequeue():
    global front
    global rear
    if front==-1 and rear==-1:
        print("Queue is empty")
    elif front==rear:
        print(queue[front],"is dequeued from queue")
        print(front,rear)
        queue.pop(0)
        front=rear=-1
    else:
        print(queue[front],"is dequeued from queue")
        queue.pop(0)
        rear-=1
def PEEK():
    if queue:
        print(queue[rear],"is the last elment in Queue")
    else:
        print("Queue is empty")

def Display():
    if queue:
        print("Queue:",queue)
    else:
        print("Queue is empty")

if __name__=="__main__":
    queue=[]
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
            Enqueue(data)
        elif ip==2:
            Dequeue()
        elif ip==3:
            PEEK()
        elif ip==4:
            Display()
        elif ip==-1:
            print("you have been exited form the Queue")
            break
        else:
            print("ivalid input")