def palindromic_substring(strs):
    n=len(strs)
    count=0
    def expand(left,right):
        local_count=0
        while left>=0 and right<n and strs[left]==strs[right]:
            local_count+=1
            left-=1
            right+=1
        return local_count
    for i in range(n):
        count+=expand(i,i)
        count+=expand(i,i+1)
    return count
print(palindromic_substring("abcc"))