# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.store = {}

        def inorder(root):
            
            if root:
                inorder(root.left)
                self.store[root.val] = 1 + self.store.get(root.val, 0)
                inorder(root.right)
        
        inorder(root)

        mode = max(self.store.values())
        ans = []
        for val in self.store:
            if self.store[val] == mode:
                ans.append(val)
        
        return ans