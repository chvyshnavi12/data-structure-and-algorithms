def missing(nums,k):
    for i in range(max(nums)):
        if i not in nums:
            k-=1
            if k==-1:
                return i
arr = [3, 5, 7, 10]
k = 6
print(missing(arr,k))
arr = [1, 4, 6, 8, 9]
k = 3
print(missing(arr,k))
def using_binary(nums,k):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        missing_nums=arr[mid]-(mid+1)
        if missing_nums<k:
            left=mid+1
        else:
            right=mid-1
    return left+k
arr = [3, 5, 7, 10]
k = 6
print(using_binary(arr,k))

