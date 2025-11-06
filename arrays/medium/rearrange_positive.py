def rearrange_positive(nums):
    positives = [x for x in nums if x >= 0]
    negatives = [x for x in nums if x < 0]

    result = []
    i = j = 0

    # alternate positive and negative
    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        i += 1
        result.append(negatives[j])
        j += 1

    # append remaining elements (if any)
    result.extend(positives[i:])
    result.extend(negatives[j:])

    return result


nums = [2, 4, 5, -1, -3, -4]
print(rearrange_positive(nums))
