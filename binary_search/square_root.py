def square_root(n):
    if n==1:
        return 1
    start=0
    end=n//2
    ans=0
    while start<=end:
        mid=(start+end)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            start=mid+1
            ans=mid
        else:
            end=mid-1
            
    return ans
print(square_root(145))