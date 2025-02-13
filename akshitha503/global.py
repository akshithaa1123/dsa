def Fun():
    a=3#loacl to scope(fun)
    print(a)#2
if __name__=="__main__":
    a=5#local variable
    print(a)#1
    Fun()
    print(a)#3
