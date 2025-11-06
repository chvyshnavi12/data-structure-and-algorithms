def longest_sub_with_sum(nums, S):
    n = len(nums)
    left = 0
    curr_sum = 0
    maxlen = 0

    for right in range(n):
        curr_sum += nums[right]

        # shrink window if sum exceeds target
        while curr_sum > S and left <= right:
            curr_sum -= nums[left]
            left += 1

        # check if window sum equals target
        if curr_sum == S:
            maxlen = max(maxlen, right - left + 1)

    return maxlen


s = 10
nums = [2, 3, 5, 1, 9]
print(longest_sub_with_sum(nums, s))
