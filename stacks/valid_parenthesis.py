def valid_parenthesis(strs):
    n=len(strs)
    map={
        "]":'[',
        '}':'{',
        ')':'('
    }
    stack=[]
    if not strs:
        return True
    for i in strs:
        if i in map:
            x=stack.pop() if stack else '#'
            if x!=map[i]:
                return False
        else:
            stack.append(i)
    return not stack
print(valid_parenthesis("()[]}"))
