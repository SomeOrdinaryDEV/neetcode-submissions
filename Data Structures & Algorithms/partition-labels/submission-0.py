class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}

        for i in range(len(s)-1,-1,-1):
            if s[i] not in last:
                last[s[i]] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size+=1
            end = max(end, last[c])
            if i == end:
                res.append(size)
                size = 0
        return res