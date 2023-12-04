class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in range(len(nums)):
            if (nums[i] == 1):
                count += 1
            else:
                res = max(res, count)
                count = 0
            if (i + 1 == len(nums)):
                res = max(res, count)
        return res