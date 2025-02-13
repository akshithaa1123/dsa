n=int(input("enter the number"))
if n<0:
    n=n*-1
total=0
while(n>0):
    total+=n%10
    n=n//10
print(total)
