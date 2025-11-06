print("hi")
def practice(nums,target):
    rows,cols=len(nums),len(nums[0])
    row=-1
    for i in range(rows):
        if nums[i][0]<=target<nums[i][-1]:
            row=i
            break
    if row==-1:
        return False
    left,right=0,cols-1
    while left<=right:
        mid=(left+right)//2
        if int(nums[mid])==target:
            return True
        elif int(nums[mid])<target:
            left=mid+1
        else:
            right=mid-1
nums=[[1,2,3],[4,5,6],[7,8,9]]
target=5

print(practice(nums,target))
    