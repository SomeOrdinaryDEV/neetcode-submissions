# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def inorder(curr, l):
            if not curr:
                return
            inorder(curr.left, l)
            l.append(curr.val)
            inorder(curr.right,l)
            return l
        inorder(root, l)
        return l[k-1]
            

