def sub_arr_xor(nums,k):
    cnt=0
    prefix=0
    freq={0:1}
    for num in nums:
        prefix^=num
        if prefix^k in freq:
            cnt+=freq[prefix^k]
        freq[prefix]=freq.get(prefix,0)+1
    return cnt
nums = [4, 2, 2, 6, 4]
k = 6
print(sub_arr_xor(nums,k))