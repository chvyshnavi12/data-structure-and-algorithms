def floor_nth_root(x, n):
    start, end = 1, x
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if mid ** n == x:
            return mid
        elif mid ** n < x:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

# Example
print(floor_nth_root(28, 3))  # Output: 3 (since 3³=27 < 28)
