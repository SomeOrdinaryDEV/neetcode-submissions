class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)

        for i in range(r):
            sum = numbers[l] + numbers[r-1]
            if sum == target:
                return [l+1,r]
            if sum > target:
                r -= 1
            if sum < target:
                l +=1
