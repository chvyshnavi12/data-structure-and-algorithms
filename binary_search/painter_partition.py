def can_paint(C, A, max_units):
    painters = 1
    total = 0

    for length in C:
        if length > max_units:
            return False

        if total + length > max_units:
            painters += 1
            total = length
            if painters > A:
                return False
        else:
            total += length

    return True


def painters_partition(A, B, C):
    MOD = 10000003

    left, right = max(C), sum(C)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can_paint(C, A, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return (ans * B) % MOD
