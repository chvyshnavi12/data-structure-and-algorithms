def max_cons(nums):
    n=len(nums)
    cnt=0
    maxcnt=0
    for i in nums:
        if i==1:
            cnt+=1
            maxcnt=max(cnt,maxcnt)
        else:
            cnt=0
    return maxcnt
nums = [1, 1, 0, 0, 1, 1, 1, 0]
print(max_cons(nums))