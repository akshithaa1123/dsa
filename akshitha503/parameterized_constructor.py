class Human:
    def __init__(self,name,branch,roll_num,age):
        self.name=name
        self.branch=branch
        self.roll_num=roll_num
        self.age=age
    def Display(self):
        print(self.name,self.branch,self.roll_num,self.age)
if __name__=="__main__":
    print("person's info")
    h1=Human("X","ece",1,19)
    h2=Human("Y","cse",2,20)
    
    h1.Display()
    h2.Display()
