def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for row in matrix:
        # Binary search only if target can be in this row
        if row[0] <= target <= row[-1]:
            left, right = 0, m - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

    return False
