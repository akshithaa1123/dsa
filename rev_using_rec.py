def rev(n,r):
    if n<=0:
        print(r)
        return
    rem=n%10
    r=r*10+rem
    rev(n//10,r)
r=0        
rev(5354,r)