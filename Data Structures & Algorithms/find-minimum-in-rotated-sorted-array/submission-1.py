class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r)//2
    
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[r]


#[4,5,0,1,2,3] -> 0, 5 | 2