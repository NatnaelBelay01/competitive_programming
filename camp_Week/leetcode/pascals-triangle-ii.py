class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        def rec( n , ans):
            if n == 1:
                return ans
            ans.append(1)
            for idx in range(len(ans) - 2 , 0 , -1):
                ans[idx] = ans[idx] + ans[idx-1]
            return rec(n-1 , ans)

        ans = [1 , 1]

        return rec(rowIndex , ans)
        