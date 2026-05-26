# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def check(curr, curMax):
            if not curr:
                return 0
            if curr.val>=curMax:
                count = 1
            else:
                count = 0

            curMax = max(curr.val, curMax)    
            
            count += check(curr.left,curMax)
            count += check(curr.right,curMax)
            return count
        
        
        return check(root, root.val)       
