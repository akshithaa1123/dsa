n=int(input("enter the number"))
if n<0:
    n=n*-1
count=0
while(n>0):
    n=n//10
    count+=1
print(count)

#taking input as string

n=str(input())
if (n[0]=='-'):
    print(len(n)-1)
else:
    print(len(n))
