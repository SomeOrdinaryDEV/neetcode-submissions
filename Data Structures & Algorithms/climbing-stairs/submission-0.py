class Solution:
    vals = {}
    def _climbStairs(self, n, vals):
        if n in vals:
            return vals[n]
        if n==2:
            return 2
        if n==1:
            return 1
        
        
        vals[n] = self._climbStairs(n-1, vals) + self._climbStairs(n-2, vals)
        return vals[n]
    
    def climbStairs(self, n: int):
        return self._climbStairs(n, {})






#n [3 -> [3-1], [3-2] []]