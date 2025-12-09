def expand(s,left,right):
    while left>=0 and right<n and s[left]==s[right]:
        left-=1
        right+=1
    return [left+1,right]

def fun(s):
    for i in range(len(s)):
        l1,r1=expand(i,i)
        l2,r2=expand(i,i+1)
        start,end=0,0
        if r1-l1>start-end:
            start,end=l1,r1
        if r2-l2>start-end:
            start,end=l2,r2
    return s[start:end]
