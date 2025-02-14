def LinearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return "key found"
    return "key not found"



arr=list(map(int,input().split()))
key=int(input("enter value to be searched"))
print(LinearSearch(arr,key))