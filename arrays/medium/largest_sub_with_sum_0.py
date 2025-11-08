def largest_sub_with_sum_zero(nums):
    prefix_sum=0
    sum_indices={}
    max_len=0
    for i,num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum==0:
            max_len=i+1
        elif prefix_sum in sum_indices:
            max_len=max(max_len,i-sum_indices[prefix_sum])
        else:
            sum_indices[prefix_sum]=i
    return max_len
arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(largest_sub_with_sum_zero(arr))


    