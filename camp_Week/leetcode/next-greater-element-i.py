class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = {}
        stack = []
        for i, val in enumerate(nums2):
            while (stack and stack[-1] < val):
                check[stack.pop()] = val
            stack.append(val)
        while (stack):
            check[stack.pop()] = -1
        ans = []
        for i in nums1:
            ans.append(check[i])
        return ans