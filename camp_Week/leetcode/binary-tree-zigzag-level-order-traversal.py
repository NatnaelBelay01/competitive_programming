# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        



        self.ans = []

        def max_dep(root , n):
            
            if root:
                return max(max_dep(root.left, n+1),  max_dep(root.right, n+1))
            else:
                return n - 1
        
        d = max_dep(root , 1)
        print(d)
        self.ans = []
        for i in range(d):
            self.ans.append([])


        def rec(root, n):
            if root:
                self.ans[n].append(root.val)
                rec(root.left , n+1)
                rec(root.right , n+1)

        rec(root, 0)
        

        for i in range(len(self.ans)):
            if i % 2 == 1:
                self.ans[i] = self.ans[i][::-1]

        return self.ans

