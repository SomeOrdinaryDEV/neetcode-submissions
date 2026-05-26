class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for item in nums:
            freq[item] = freq.get(item, 0) + 1
        res = [[] for _ in range(len(nums)+1)]
        for item in freq:
            res[freq.get(item)].append(item)
            print(item, freq.get(item))
        final_res = []
        x = k
        for i in range(len(res)-1,-1,-1):
            if res[i] == []:
                continue
            for item in res[i]:
                if x!=0:
                    x = x-1
                    final_res.append(item)
        return final_res