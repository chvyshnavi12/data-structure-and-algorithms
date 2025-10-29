def trapping_rainwater(height):
    n=len(height)
    left=0
    right=n-1
    leftmax=0
    rightmax=0
    result=0
    while left<right:
        leftmax=max(leftmax,height[left])
        rightmax=max(rightmax,height[right])
        if leftmax<rightmax:
            result+=leftmax-height[left]
            left+=1
        else:
            result+=rightmax-height[right]
            right-=1
    return result
print(trapping_rainwater([4,2,0,3,2,5]))
