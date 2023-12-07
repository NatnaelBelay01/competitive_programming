class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = set(i for i in nums)
        for num in range(len(nums) + 1):
            if(num not in check):
                return num