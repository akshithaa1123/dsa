def BinarySearch(arr,key,l,r):
    while(l<=r):
        mid=(l+r)//2
        if arr[mid]==key:
            return "key found"
        elif key>arr[mid]:
            l=mid+1
        elif key<arr[mid]:
            r=mid-1
        
    return "key not found"



arr=list(map(int,input().split()))
key=int(input("enter value to be searched"))
arr.sort()
print(BinarySearch(arr,key,0,len(arr)-1))