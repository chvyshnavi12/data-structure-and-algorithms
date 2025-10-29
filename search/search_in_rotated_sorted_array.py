def search_in_rotated_sorted(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if nums[left]<nums[mid]:
            if nums[left]<=target<=nums[target]:
                right=mid-1
            else:
                left=mid+1
        else:
            if nums[right]<=target<=nums[mid]:
                left=mid+1
            else:
                right=mid-1
    return -1


