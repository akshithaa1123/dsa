#FOR LOOPS
x=5
for i in range(1,x):
    print(i,end=" ")

print('odd')
#odd numbers
n=10
for i in range(1,n):
    if(i%2!=0):
        print(i)

#odd without if conditions
for i in range(1,n,2):
    print(i)

#even numbers
for i in range(0,n,2):
    print(i)

#reverse 
for i in range(n,0,-1):
    print(i)

#odd numbers in reverse
for i in range(n,0,-1):
    if(i%2!=0):
        print(i)





      
