def PUSH(data):
    if len(stack)<capacity:
        stack.append(data)
        print(data,"is pushed into the stack")
    else:
        print("stack overflow")
def POP():
    if stack:
        print(stack[-1],"is popped from the stack")
        stack.pop()
    else:
        print("stack underflow")
def PEEK():
    if stack:
        print(stack[-1],"is the top elment in stack")
    else:
        print("stack is empty")

def Display():
    if stack:
        print("stack:",stack)
    else:
        print("stack is empty")

if __name__=="__main__":
    stack=[]
    capacity=int(input("enter capacity of stack:"))
    print("welcome to stack operation")

    print("enter 1 to PUSH an element into stack")
    print("enter 2 to POP an element into stack")
    print("enter 3 to show PEEK of the stack")
    print("enter 4 to DISPLAY elements of stack")
    print("enter -1 to EXIT from stack\n")
    while True:
        ip=int(input("enter your choice:"))
        if ip==1:
            data=int(input("enter the value to be pushed into stack:"))
            PUSH(data)
        elif ip==2:
            POP()
        elif ip==3:
            PEEK()
        elif ip==4:
            Display()
        elif ip==-1:
            print("you have been exited form the stack")
            break
        else:
            print("ivalid input")