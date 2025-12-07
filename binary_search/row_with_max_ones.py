def rowWithMax1s(mat):
    n = len(mat)
    m = len(mat[0])
    max_ones = 0
    max_row = -1

    for i in range(n):
        # binary search for first 1
        low, high = 0, m - 1
        first_one = m

        while low <= high:
            mid = (low + high) // 2
            if mat[i][mid] == 1:
                first_one = mid
                high = mid - 1
            else:
                low = mid + 1

        ones = m - first_one
        if ones > max_ones:
            max_ones = ones
            max_row = i

    return max_row
