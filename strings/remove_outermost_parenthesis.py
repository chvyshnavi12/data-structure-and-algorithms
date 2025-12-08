def remove_outermost_parenthesis(x):
    depth=0
    res=[]
    for c in x:
        if c=='(':
            if depth>0:
                res.append("(")
            depth+=1
        else:
            depth-=1
            if depth>0:
                res.append(")")
    return "".join(res)
print(remove_outermost_parenthesis("((()))"))