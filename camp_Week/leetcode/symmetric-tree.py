# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        self.lst1 = []


        def preorder(root):

            if root:
                self.lst1.append(root.val)
                preorder(root.left)
                preorder(root.right)
            else:
                self.lst1.append(None)
        

        def pre(root):

            if root:
                self.lst1.append(root.val)
                pre(root.right)
                pre(root.left)
            else:
                self.lst1.append(None)



          
        pre(root.right)
        ch1 = self.lst1[:]
        self.lst1 = []
        preorder(root.left)




        for idx in range(max( len(ch1) , len(self.lst1) )):

            if(idx >= len(ch1) or idx >= len(self.lst1)):
                return False
            if(ch1[idx] != self.lst1[idx]):
                return False

        return True