def valid_parenthesis(input):
    n=len(input)
    strs={
        ']':'[',
        '}':'{',
        ')':'('
    }
    stack=[]
    for i in input:
        
        if i in strs:
            x=stack.pop()
            if strs[i]!=x:
                return False
        else:
            stack.append(i)
    return not stack
print(valid_parenthesis("()[]"))
