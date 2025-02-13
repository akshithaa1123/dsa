# to check if a number is prime
n=int(input("enter the number to check"))
flag=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        flag=False
        break
if flag:
    print("prime number")
else:
    print("not a prime number")
        
