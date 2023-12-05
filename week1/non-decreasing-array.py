class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        idx = 1
        length = len(nums)
        count = 0
        
        while (idx < len(nums)):
            if (nums[idx-1] > nums[idx]):

                before = nums[idx - 2] if idx - 2 >= 0 else float('-inf')
                after = nums[idx + 1] if idx + 1 < length else float('inf')
            
                if before <= nums[idx - 1] <= after or before <= nums[idx] <= after:
                    count += 1
                else:
                    return False

            idx += 1
        return count <= 1