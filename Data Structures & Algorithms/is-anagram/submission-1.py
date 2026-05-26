class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def counter(s):
            countMap = {}
            for c in s:
                if c not in countMap:
                    countMap[c] = 1
                else:
                    countMap[c] += 1
            return countMap
        
        mapA = counter(s)
        mapB = counter(t)

        return mapA==mapB
        


