def permutation(strs):
    n=len(strs)
    result=[]
    def backtrack(path,seen):
        if len(path)==n:
            result.append(path[:])
        for i in strs:
            if i in seen:
                continue
            path.append(i)
            seen.add(i)
            backtrack(path,seen)
            path.pop()
            seen.remove(i)
    backtrack([],set())
    return result
result=permutation("vyshu")
for i in result:
    print(i)
            