class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        map_a = {}
        map_b = {}
        for c in s:
            if c in map_a:
                map_a[c] += 1
            else:
                map_a[c] = 1
        
        for c in t:
            if c in map_b:
                map_b[c] += 1
            else:
                map_b[c] = 1
        return map_a==map_b