class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            count = 0
            for _ in range(32):
                if n&1==1:
                    count +=1
                n = n>>1
            return count

        res =  []

        for i in range(n+1):
            res.append(count(i))
        return res