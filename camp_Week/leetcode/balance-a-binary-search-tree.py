# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.nums = []

        def rec(root):
            if root:
                rec(root.left)
                self.nums.append(root.val)
                rec(root.right)

        def build(l, r):
            if l > r:
                return None
            idx = (r + l) // 2 

            left = build(l, idx - 1)
            right = build(idx+1, r)
            return TreeNode(self.nums[idx], left , right)

        rec(root)
        print(self.nums)

        return build(0, len(self.nums) - 1)