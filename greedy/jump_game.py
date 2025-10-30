def jump_game(nums):
    max_reach=0
    for i,num in enumerate(nums):
        if i>max_reach:
            return False
        max_reach=max(max_reach,num+i)
    return True
print(jump_game([2,3,1,1,4]))
