def string_to_integer(strs):
    n=len(strs)
    sign=1
    i=0
    if strs[i] in ["-","+"]:
        if strs[i]=='-':
            sign=-1
        i+=1
    
    result=0
    while i<n and strs[i].isdigit():
        
        result=result*10+int(strs[i])
        i+=1
    max_num=2**31-1
    min_num=-2**32
    if result<min_num:
        result=min_num
    if result>max_num:
        result=max_num
    return result
print(type(string_to_integer("-123")))

    
