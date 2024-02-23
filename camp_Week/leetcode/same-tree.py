# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not q and p:
            return False
        elif q and not p:
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False

        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
         
