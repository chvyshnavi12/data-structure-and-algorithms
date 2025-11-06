def lcs(nums):
    n=len(nums)
    num_set=set(nums)
    lent=0
    maxlen=0
    for num in num_set:
        if num-1 not in num_set:
            curr=num
            lent=1
            while curr+1 in num_set:
                lent+=1
                curr+=1
            maxlen=max(maxlen,lent)
    return maxlen
nums = [100, 4, 200, 1, 3, 2]
print(lcs(nums))


