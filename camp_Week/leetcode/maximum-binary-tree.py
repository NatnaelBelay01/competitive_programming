# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def rec(i, j):
            if i >= j:
                return None
            check = float('-inf')
            p = i
            for idx in range(i , j):
                if check < nums[idx]:
                    check = nums[idx]
                    p = idx
                
            root = TreeNode(nums[p])
            root.right = rec(p+1 , j)
            root.left = rec(i, p)
            return root
    
        return rec(0, len(nums))