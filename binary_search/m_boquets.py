def canMakeBouquets(nums, m, k, day):
    count = 0  # count of adjacent bloomed roses
    bouquets = 0

    for bloom in nums:
        if bloom <= day:
            count += 1
            if count == k:
                bouquets += 1
                count = 0
        else:
            count = 0  # reset if rose not bloomed yet

    return bouquets >= m


def minDays(nums, m, k):
    n = len(nums)
    if m * k > n:
        return -1  # not enough roses to form bouquets

    low, high = min(nums), max(nums)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if canMakeBouquets(nums, m, k, mid):
            ans = mid
            high = mid - 1  # try smaller day
        else:
            low = mid + 1   # need more days

    return ans


# Example
nums = [1, 10, 3, 10, 2]
m = 3
k = 1
print(minDays(nums, m, k))
