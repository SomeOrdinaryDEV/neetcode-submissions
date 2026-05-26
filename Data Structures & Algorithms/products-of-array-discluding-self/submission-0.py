class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultFront = []
        resultBack = []
        final = []
        product = 1
        for i in range(0, len(nums)):
            product = product*nums[i]
            resultFront.append(product)
        product = 1
        for i in range(len(nums)-1,-1, -1):
            product = product*nums[i]
            resultBack.append(product)
        resultBack = (resultBack[::-1])

        resultFront.insert(0,1)
        resultBack.append(1)
        print(resultFront)
        print(resultBack)

        for i in range(0, len(resultFront)-1):
            final.append(resultFront[i]*resultBack[i+1])
        return final

