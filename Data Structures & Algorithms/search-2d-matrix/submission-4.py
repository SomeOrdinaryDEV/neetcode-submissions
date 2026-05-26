class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        # Step 1: find correct row
        row = -1
        for i in range(n):
            if target <= matrix[i][m - 1]:
                row = i
                break
        
        if row == -1:
            return False
        
        # Step 2: binary search in that row
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False