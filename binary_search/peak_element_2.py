def findPeakGrid(mat):
    n, m = len(mat), len(mat[0])
    left, right = 0, m - 1

    while left <= right:
        mid = (left + right) // 2

        # Find row with maximum element in mid column
        max_row = 0
        for r in range(n):
            if mat[r][mid] > mat[max_row][mid]:
                max_row = r

        # Get left and right neighbors safely
        left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
        right_val = mat[max_row][mid + 1] if mid + 1 < m else -1
        curr = mat[max_row][mid]

        # Check peak
        if curr > left_val and curr > right_val:
            return [max_row, mid]

        # Move search direction
        if left_val > curr:
            right = mid - 1
        else:
            left = mid + 1

    return [-1, -1]  # Should never execute
