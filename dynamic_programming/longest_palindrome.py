def palindrome_partition(strs):
    n=len(strs)
    def expand(left,right):
        while left>=0 and right<n and strs[left]==strs[right]:
            left-=1
            right+=1
        return (left+1,right)
    start,end=0,0
    for i in range(n):
        l1,r1=expand(i,i)
        l2,r2=expand(i,i+1)
        if r1-l1>end-start:
            start,end=l1,r1
        if r2-l2>end-start:
            start,end=l2,r2
    return strs[start:end]
strs="cbbd"
print(palindrome_partition(strs))

    