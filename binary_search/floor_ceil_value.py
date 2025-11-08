def floor_ceil_val(nums,target):
    n=len(nums)
    left,right=0,n-1
    ciel=nums[0]
    floor=nums[0]
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]<target:
            floor=nums[mid]
            left=mid+1
        else:
            ciel=nums[mid]
            right=mid-1
    return [floor,ciel]
nums =[3, 4, 4, 7, 8, 10]
x= 5
print(floor_ceil_val(nums,x))

