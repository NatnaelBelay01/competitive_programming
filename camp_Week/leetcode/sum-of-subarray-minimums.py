class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10 ** 9) + 7
        def small(arr):
            stack = []
            check = {}
            for idx , val in enumerate(arr):
                while stack and val < arr[stack[-1]]:
                    temp = stack.pop()
                    check[temp] = idx - temp
                stack.append(idx)
            for val in stack:
                check[val] = -1
            ans = []
            for idx in range(len(arr)):
                ans.append(check[idx])
            return ans
        def big(arr):
            stack = []
            check = {}
            for idx , val in enumerate(arr):
                while stack and val <= arr[stack[-1]]:
                    temp = stack.pop()
                    check[temp] = idx - temp
                stack.append(idx)
            for val in stack:
                check[val] = -1
            ans = []
            for idx in range(len(arr)):
                ans.append(check[idx])
            return ans[::-1]

        before , after = big(arr[::-1]) , small(arr)

        print(after , '\n' , before)

        res = 0

        for idx in range(len(arr)):
            if(before[idx] < 0):
                left = idx
            else:
                left = before[idx] - 1

            if(after[idx] < 0):
                right = len(arr) - idx
            else:
                right = after[idx]
            res += (left + 1) * right * arr[idx]

        return res % MOD


                