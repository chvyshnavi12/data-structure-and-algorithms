def is_station(a,d):
    n=len(a)
    cnt=0
    for i in range(n-1):
        gap=a[i+1]-a[i]
        cnt+=int(gap/d)
    return cnt

def gas_station(a,k):
    left,right=0,a[-1]-a[0]
    eps=1e-6
    while right-left>eps:
        mid=(left+right)/2.0
        if is_station(a,mid)>k:
            left=mid
        else:
            right=mid
    return right
n = 10
arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
k = 9
print(gas_station(arr,k))
