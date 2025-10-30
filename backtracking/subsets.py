def subsets(nums):
    n=len(nums)
    result=[]
    def backtrack(start,path):
        result.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
        return result
    backtrack(0,[])
    result.sort(key=len)
    return result
print(subsets([1,2,3]))
