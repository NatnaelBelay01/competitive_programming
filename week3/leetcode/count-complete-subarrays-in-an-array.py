class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        hash_map = {}
        count = 0
        for idx in range(len(nums)):
            hash_map[nums[idx]] = 1 + hash_map.get(nums[idx], 0)
        
        check = {}

        for left in range(len(nums)):

            check = {}
            for right in range(left, len(nums)):
                check[nums[right]] = 1 + check.get(nums[right], 0)
            if(len(check) >= len(hash_map)):
                right = len(nums) - 1
                
                while(right >= left):
                    if(len(check) == len(hash_map)):
                        count += 1
                    check[nums[right]] -= 1
                    if(check[nums[right]] == 0):
                        check.pop(nums[right])
                    right -= 1
        return count

        