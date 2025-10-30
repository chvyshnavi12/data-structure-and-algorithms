def palindrome_partitioning(strs):
    n=len(strs)
    result=[]
    def ispalindrome(tt):
        return tt==tt[::-1]
    def backtrack(start,path):
        if start==n:
            result.append(path[:])
            return
        for end in range(start,n):
            sub=strs[start:end+1]
            if ispalindrome(sub):
                path.append(sub)
                backtrack(end+1,path)
                path.pop()
        return result
    backtrack(0,[])
    return result
print(palindrome_partitioning("aab"))
            