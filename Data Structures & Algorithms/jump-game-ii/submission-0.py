class Solution:
    def jump(self, nums: List[int]) -> int:
        goal, steps = len(nums)-1, 0
        l, r = 0, 0
        while r<goal:
            temp = 0
            for i in range(l,r+1):
                temp = max(temp, i+nums[i])
            l = r+1
            r = temp
            steps += 1
        return steps
