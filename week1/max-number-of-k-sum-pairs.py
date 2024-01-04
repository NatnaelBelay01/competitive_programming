class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        first , last = 0 , len(nums) - 1

        count = 0

        
        while(first < last):
            if (nums[first] + nums[last] < k):
                first += 1
            elif (nums[first] + nums[last] > k):
                last -= 1
            else:
                count += 1
                last -= 1
                first += 1
        return count