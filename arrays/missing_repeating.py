def find_missing_repeating(n,nums):
    result=[]
    for i in range(1,n+1):
        if i not in nums:
            result.append(i)
    seen=set()
    for i in nums:
        if i in seen:
            result.append(i)
        seen.add(i)
    return result
result=find_missing_repeating(5,[1, 3, 3, 5, 4])
print("missing number is:"+str(result[0])+"\n"+"repeated number is:"+str(result[1]))
                   

