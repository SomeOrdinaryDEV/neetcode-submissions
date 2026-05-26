class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = nums.copy(), nums.copy()
        product = 1
        for i in range(len(nums)):
            product = product * prefix[i]
            prefix[i] = product
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product = product * suffix[i]
            suffix[i] = product
        prefix.insert(0,1)
        suffix.append(1)
        i, j = 0, 1
        res = []
        while j < len(suffix):
            res.append(prefix[i] * suffix[j])
            i+=1
            j+=1
        return res
        




#[1, a, a*b, a*b*c]
#[b*c, a*c, a*b] -> target
#[a*b*c, b*c, c, 1]