class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        ans = []
        def backtrack(i, path):

            if len(path)==k:
                ans.append(path[:])
                return
            
            for choice in range(i+1, n+1):
                path.append(choice)
                backtrack(choice, path)
                path.pop()

        ans = []
        backtrack(0 , [])

        return ans



        # [1 , 2] [ 1 , 3] [1 , 4]
        #  [2, 3] [2 , 4]
        #  [3 , 4]

