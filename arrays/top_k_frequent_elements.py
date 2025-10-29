import heapq
from collections import Counter
def top_k_frequent_elements(nums,k):
    result=[]
    counter=Counter(nums)
    top_k=heapq.nlargest(k,counter.items(),key=lambda x:x[1])
    for num,freq in top_k:
        result.append(num)
    return result
print(top_k_frequent_elements([1,2,1,2,1,2,3,1,3,2],2))