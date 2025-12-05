def can_split(arr, k, limit):
    subarrays = 1
    curr_sum = 0

    for num in arr:
        if curr_sum + num > limit:
            subarrays += 1
            curr_sum = num
            if subarrays > k:
                return False
        else:
            curr_sum += num

    return True


def split_array(arr, k):
    left, right = max(arr), sum(arr)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_split(arr, k, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
