a=6#local variable
def Fun():
    #print(a)#2
    a=5
    print(a)#3
if __name__=="__main__":
    print(a)#1
    Fun()
    print(a)#4