# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []
        

        store = {}
        self.minmax = [0, 0]

        def rec(root, n, m):

            if root:
                self.minmax[0] = min(self.minmax[0], n)
                self.minmax[1] = max(self.minmax[1], n)
                if n not in store:
                    store[n] = []
                store[n].append( [m , root.val] )
                rec(root.right, n+1, m+1)
                rec(root.left, n-1, m+1)
        
        res = []
        rec(root, 0, 0)
        print(store)
        print(self.minmax)
        for val in range(self.minmax[0] , self.minmax[1] + 1):
            if len(store[val]) > 1:
                store[val].sort(key=lambda x : (x[0], x[1]))
                temp = []
                for i in store[val]:
                    temp.append(i[1])
                res.append(temp)
            else:
                res.append([ store[val][0][1] ])
        print(res)
        return res