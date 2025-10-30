def combination_sum(nums,target):
    n=len(nums)
    result=[]
    def backtrack(start,path,total):
        if total==target:
            result.append(path[:])
            return
        if total>target:
            return
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i,path,total+nums[i])
            path.pop()
        return result
    backtrack(0,[],0)
    return result
print(combination_sum([1, 2, 3, 4, 5, 6], 6))

def combination_sum(nums, target):
    result = []
    nums.sort()  # optional, helps avoid duplicates

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(nums)):
            # Skip duplicates (if nums has repeating values)
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path, total + nums[i])  # ✅ i+1 → move to next element
            path.pop()

        return result

    backtrack(0, [], 0)
    return result


print(combination_sum([1, 2, 3, 4, 5, 6], 6))
