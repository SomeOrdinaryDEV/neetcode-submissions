class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for i in range(len(nums)):
            count[nums[i]] += 1
        p = 0
        for num in count:
            while count[num]>0:
                nums[p] = num
                p += 1
                count[num] -= 1

