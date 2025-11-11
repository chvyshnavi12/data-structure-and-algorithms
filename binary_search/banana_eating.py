import math

def banana_eating(nums, h):
    start, end = 1, max(nums)
    ans = end

    while start <= end:
        mid = (start + end) // 2
        hours = 0   # reset for each speed test

        for pile in nums:
            hours += math.ceil(pile / mid)

        if hours <= h:   # valid speed, try slower
            ans = mid
            end = mid - 1
        else:            # too slow, need faster speed
            start = mid + 1

    return ans


# Example
nums = [7, 15, 6, 3]
h = 8
print(banana_eating(nums, h))
