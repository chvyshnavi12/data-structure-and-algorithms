def subsets(nums):
    n=len(nums)
    result=[]
    def backtrack(path,seen):
        if len(path)==n:
            result.append(path[:])
        for i in nums:
            if i not in seen:
                path.append(i)
                seen.add(i)
                backtrack(path,seen)
                path.pop()
                seen.remove(i)
        return result
    backtrack([],set())
    return result
print(subsets([1,2,3]))
