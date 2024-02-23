# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.res = []

        def inorder(root):
            
            if root:
                inorder(root.left)
                self.res.append(root.val)
                inorder(root.right)
        inorder(root)
        
        if len(set(self.res)) < len(self.res):
            return False

        return sorted(self.res) == self.res

