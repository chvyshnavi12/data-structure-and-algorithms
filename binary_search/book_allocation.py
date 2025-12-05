def check(nums, m, limit):
    cnt = 1
    curr = 0

    for pages in nums:
        if curr + pages > limit:
            cnt += 1
            curr = 0
        curr += pages

    return cnt <= m


def book(nums, m):
    left, right = max(nums), sum(nums)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if check(nums, m, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans
