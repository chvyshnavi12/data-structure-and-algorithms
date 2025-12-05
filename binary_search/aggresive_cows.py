def canplace(k, nums, dist):
    cnt = 1
    curr = nums[0]

    for i in nums[1:]:
        if i - curr >= dist:
            cnt += 1
            curr = i
        if cnt == k:
            return True

    return False


def cow(k, nums):
    nums.sort()
    left, right = 1, nums[-1] - nums[0]
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if canplace(k, nums, mid):
            ans = mid      # distance possible → try bigger
            left = mid + 1
        else:
            right = mid - 1

    return ans


k = 4
nums = [0, 3, 4, 7, 10, 9]
print(cow(k, nums))
