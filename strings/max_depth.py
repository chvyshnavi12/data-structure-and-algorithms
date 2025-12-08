def max_depth(s):
    depth,max_depth=0,0
    for i in s:
        if i=='(':
            depth+=1
            max_depth=max(depth,max_depth)
        if i==')':
            depth-=1
    return max_depth
s = "(1+(2*3)+((8)/4))+1"
print(max_depth(s))