def count_leq(row, x):
    """Return how many numbers in the sorted row are <= x."""
    left, right = 0, len(row) - 1
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        if row[mid] <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans + 1   # because ans is index (0-based)


def matrixMedian(mat):
    r = len(mat)
    c = len(mat[0])

    # Search range: min element to max element
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)

    target = (r * c) // 2  # median index in sorted order

    while low <= high:
        mid = (low + high) // 2

        # Count how many numbers <= mid
        count = 0
        for row in mat:
            count += count_leq(row, mid)

        # Move binary search
        if count > target:
            high = mid - 1
        else:
            low = mid + 1

    return low
