class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for digit in digits:
            s = s+str(digit)
        sum = str(int(s) + 1)
        res = []
        for char in sum:
            res.append(int(char))
        
        return res

