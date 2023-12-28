class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        

        nums_cpy = sorted(nums)
        store = {}

        for idx in range(len(nums_cpy)):
            if (nums_cpy[idx] not in store):
                store[nums_cpy[idx]] = idx
        
        for idx in range(len(nums)):
            nums[idx] = store[nums[idx]]

        return nums