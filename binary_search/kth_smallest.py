def kthElement(arr1, arr2, k):
    n, m = len(arr1), len(arr2)

    # Ensure arr1 is the smaller array
    if n > m:
        return kthElement(arr2, arr1, k)

    # Low = at least 0 elements from arr1
    # High = at most k elements from arr1 (but not more than n)
    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1

        l1 = arr1[cut1 - 1] if cut1 > 0 else float("-inf")
        r1 = arr1[cut1] if cut1 < n else float("inf")

        l2 = arr2[cut2 - 1] if cut2 > 0 else float("-inf")
        r2 = arr2[cut2] if cut2 < m else float("inf")

        # Correct position
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        # Move left in arr1
        elif l1 > r2:
            high = cut1 - 1

        # Move right in arr1
        else:
            low = cut1 + 1
