def check(weights,days,k):
    curr=0
    curr_days=1
    for i in weights:
        if curr+i>k:
            curr_days+=1
            curr=0
        curr+=i
    return curr_days<=days
def cap(weights,days):
#n=len(nums)
    left,right=max(weights),sum(weights)
    k=right
    while left<=right:
        mid=(left+right)//2
        if(check(weights,days,mid)):
            k=mid
            right=mid-1
        else:
            left=mid+1
    return k
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(cap(weights,days))
weights = [3, 2, 2, 4, 1, 4]
days = 3
print(cap(weights,days))


        
