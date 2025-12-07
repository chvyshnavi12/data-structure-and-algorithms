def ispossible(a,k,x):
    cnt=1
    y=0
    for i in a:
        if y+i>x:
            cnt+=1
            y=0
        y+=i
    return cnt<=k
def split(a,k):
    n=len(a)
    left,right=max(a),sum(a)
    ans=0
    cnt=0
    while left<=right:
        mid=(left+right)//2
        if ispossible(a,k,mid):
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans
a = [1, 2, 3, 4, 5]
k = 3
print(split(a,k))
a = [3,5,1]
k = 3
print(split(a,k))

