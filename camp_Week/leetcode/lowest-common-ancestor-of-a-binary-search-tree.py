# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.checked = set()
        self.res = None

        def first(root, val):

            if root:
                self.checked.add(root)
                if root.val > val:
                    return first(root.left, val)
                elif root.val < val:
                    return first(root.right, val)
                else:
                    return root


        def second(root, val):
            if root:
                print('Hey' , root.val)
                if root in self.checked:
                    self.res = root
                if root.val > val:
                    return second(root.left, val)
                elif root.val < val:
                    return second(root.right, val)
                else:
                    return root
        
        cp1 = root
        first(cp1, q.val)

        cp2 = root
        second(cp2, p.val)

        return self.res
