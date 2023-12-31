class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        
        for idx, val in enumerate(nums):
            if target - val in store:
                return [idx, store[target - val]]
            store[val] = idx 