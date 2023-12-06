class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        ans = []
        for val in nums:
            count[val] = 1 + count.get(val, 0)
        occurance = len(nums) // 3
        for val in count:
            if (count[val] > occurance):
                ans.append(val)
        return ans