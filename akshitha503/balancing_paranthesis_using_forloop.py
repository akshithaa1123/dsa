def isBalanced(s):
    stk=[]
    pairs={'}':'{',']':'[',')':'('}

    for val in s:
        if val in '{[(':
            stk.append(val)
        elif val in ']})':
            if not stk or stk[-1]!=pairs[val]:
                return 'Not Balanced'
            else:
                stk.pop()
    
    return 'Balanced' if len(stk)==0 else 'not balanced'
if __name__=="__main__":
    s=input()
    print(isBalanced(s))