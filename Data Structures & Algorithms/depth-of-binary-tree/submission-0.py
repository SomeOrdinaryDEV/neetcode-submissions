# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], maxx = 0) -> int:
        if not root:
            return maxx
        if root:
            maxx += 1
            maxx = max(self.maxDepth(root.left, maxx), self.maxDepth(root.right, maxx))

        return maxx