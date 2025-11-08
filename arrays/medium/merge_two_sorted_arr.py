def merge(num1,num2):
    
    result=[]
    num1.sort()
    num2.sort()
    n,m=len(num1),len(num2)
    i,j=0,0
    while (i<n) and (j<m):
        if num1[i]<num2[j]:
            result.append(num1[i])
            i+=1
        else:
            result.append(num2[j])
            j+=1
    result.extend(num1[i:])
    result.extend(num2[j:])
    return result
nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]
print(merge(nums1,nums2))