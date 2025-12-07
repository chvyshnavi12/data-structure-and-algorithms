def median(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    n, m = len(arr1), len(arr2)
    total = n + m
    half = total // 2

    left, right = 0, n

    while left <= right:
        cut1 = (left + right) // 2
        cut2 = half - cut1

        l1 = arr1[cut1 - 1] if cut1 > 0 else float("-inf")
        r1 = arr1[cut1] if cut1 < n else float("inf")

        l2 = arr2[cut2 - 1] if cut2 > 0 else float("-inf")
        r2 = arr2[cut2] if cut2 < m else float("inf")

        if l1 <= r2 and l2 <= r1:
            if total % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return min(r1, r2)
        elif l1 > r2:
            right = cut1 - 1
        else:
            left = cut1 + 1
