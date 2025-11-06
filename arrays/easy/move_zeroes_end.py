def move_zeroes(nums):
    arr=[]
    zeroes=[]
    for i in nums:
        if i==0:
            zeroes.append(i)
        else:
            arr.append(i)
    arr.extend(zeroes)
    return arr
nums = [0,1,0,3,12]
print(move_zeroes(nums))