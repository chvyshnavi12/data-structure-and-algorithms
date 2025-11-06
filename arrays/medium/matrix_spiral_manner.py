def spiral_print(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Step 1: Traverse left → right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Step 2: Traverse top → bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Step 3: Traverse right → left (if still rows left)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Step 4: Traverse bottom → top (if still cols left)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_print(matrix))
