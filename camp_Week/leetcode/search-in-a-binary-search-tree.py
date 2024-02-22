# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def rec(root):
            
            if root:
                if val > root.val:
                    return rec(root.right)
                elif val < root.val:
                    return rec(root.left)
                else:
                    return root
        
        return rec(root)