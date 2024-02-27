# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def rec(root, string):
            
            if root.right or root.left:
                if root.left:
                    rec(root.left, string + str(root.val))
                if root.right:
                    rec(root.right , string + str(root.val))
            else:
                self.ans += int(string + str(root.val))
        rec(root , "")
        return self.ans