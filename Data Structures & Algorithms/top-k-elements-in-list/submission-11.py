import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = Counter(nums)
        minHeap = []

        for num, n in numMap.items():
            heapq.heappush(minHeap, (n, num))

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return [num for freq, num in minHeap]
        