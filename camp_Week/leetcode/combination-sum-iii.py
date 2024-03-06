class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        

        # 1 , 2, 3, 4, 5, 6, ....

        ans = []


        def rec(i, path):

            if sum(path) > n or len(path) > k:
                return
            if len(path) == k and sum(path) == n:
                #the base case
                ans.append(path[:])
                return

            for j in range(i , 10):
                path.append(j)
                rec(j+1, path)
                path.pop()
        
        rec(1 , [])

        return ans


