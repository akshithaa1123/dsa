l=['a','b']
print(l)
l=[1,2,3,4]
print(l)
l=[1.2,3.2,2.4]
print(l)
l=['abc','c',1,2.5]
print(l)

#to print values of list
for i in range(0,len(l)):
    print(l[i],end=" ")
print()

for i in l:
    print(i,end=" ")
print()

#input
l1=list(map(int,input().split()))
print(l1)

#list functions
l=[1,2,3,4,5]
print(len(l))
print(sum(l))
print(max(l))
print(min(l))

l.append(6)
print(l)
l.extend([9,12,13])
print(l)
l.insert(4,8)
print(l)

l.pop()
print(l)
l.remove(9)
print(l)
l.clear()
print(l)












