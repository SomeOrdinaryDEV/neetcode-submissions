class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        numMap = {}

        for n in nums:
            if n not in numMap:
                numMap[n] = 0
            numMap[n] += 1
        for n in numMap:
            bucket[numMap[n]-1].append(n)
        
        res = []
        for i in range(len(nums)-1,-1,-1):
            if bucket[i] == []:
                bucket.pop()
                i-=1
            else:
                for n in bucket[i]:
                    res.append(n)
                i -= 1    
                
                
        return res[:k]