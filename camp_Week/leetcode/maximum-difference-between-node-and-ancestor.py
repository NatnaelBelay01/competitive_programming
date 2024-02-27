# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0


        def rec(root , n, m):
            
            if root:
                self.res = max(self.res , abs(root.val - n), abs(root.val - m)) 
                temp1 = n if n > root.val else root.val
                temp2 = m if m < root.val else root.val
                rec(root.right, temp1, temp2)
                rec(root.left , temp1, temp2)


        rec(root, root.val , root.val)
        return self.res