def search_2d_matrix(nums,target):
    row,col=len(nums),len(nums[0])
    top=0
    bottom=row-1
    index=-1
    while top<=bottom:
        mid=(top+bottom)//2
        if nums[mid][0]<=target<=nums[mid][-1]:
            index=mid
            break
        elif target<nums[mid][0]:
            bottom=mid-1
        else:
            top=mid+1
    if index==-1:
        return False
    left=0
    right=col-1
    while left<=right:
        mid=(left+right)//2
        if nums[index][mid]==target:
            return True
        elif nums[index][mid]<target:
            left=mid+1
        else:
            right=mid-1
    return False
print(search_2d_matrix([[1,2,3,4],[5,6,7,8]],6))
        
        
    