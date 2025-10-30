from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result=[]
        counter=Counter(nums)
        top_k=heapq.nlargest(k,counter.items(),key=lambda x:x[1])
        for item,freq in top_k:
            result.append(item)
        return result