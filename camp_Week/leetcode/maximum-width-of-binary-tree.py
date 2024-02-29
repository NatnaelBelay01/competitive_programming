# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:



        level = [(root, 1)]
        ans = 1

        while level:
            nextlevel = []
            temp = []

            for node in level:
                if node[0].left:
                    nextlevel.append((node[0].left, node[1] * 2))
                    temp.append(node[1] * 2)
                if node[0].right:
                    nextlevel.append((node[0].right, node[1] * 2 + 1))
                    temp.append(node[1] * 2 + 1)
            
            level = nextlevel
            if level:
                ans = max(ans , temp[-1] - temp[0] + 1)
            

        return ans
