#height=[1,7,2,5,4,7,3,6]
#7
#
#
#

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            currentArea = (right-left) * min(heights[left], heights[right])
            area = max(area,currentArea)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return area

                
