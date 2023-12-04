class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = []
        for i in range(1, l, 2):
            for j in range(nums[i-1]):
                res.append(nums[i])
        return res