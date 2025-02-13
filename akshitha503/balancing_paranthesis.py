def Balanced(s):
    stack=[]
    for ch in s:
        if ch=='{' or ch=='[' or ch=='(':
            stack.append(ch)
        elif not stack:
            return 'not balanced'
        elif ch=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
                return 'not balanced'
        elif ch==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                return 'not balanced'
        elif ch==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                return 'not balanced'
    return 'Not balanced' if stack else 'balanced'

if __name__=="__main__":
    s=input()
    print(Balanced(s))
