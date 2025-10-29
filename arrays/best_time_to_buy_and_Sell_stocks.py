def best_time(nums):
    min_sum=float("inf")
    profit=0
    for i in nums:
        if i< min_sum:
            min_sum=i
        if i-min_sum>profit:
            profit=i-min_sum
    return profit
print(best_time([7,1,5,3,6,4]))