class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        dic = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0
        }
        def convert(num):
            n = len(num)-1
            sum = 0
            for c in num:
                sum += dic[c] * 10**n
                n -= 1
            return sum
        res = convert(num1) * convert(num2)
        return str(res)
