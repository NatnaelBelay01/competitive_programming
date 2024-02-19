class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums.append(nums[i])
        
        check = {}
        stack = []

        for idx, val in enumerate(nums):

            while(stack and val > nums[stack[-1]]):
                check[stack.pop()] =  val
            stack.append(idx)

        for val in stack:
            check[val] = -1
        
        ans = []

        for i in range(n):
            ans.append(check[i])
        
        return ans
