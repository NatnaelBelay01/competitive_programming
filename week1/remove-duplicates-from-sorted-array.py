class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = 1
        idx = 1
        count = 1

        while (idx < len(nums)):
            while(temp < len(nums) and nums[temp] <= nums[idx - 1]):
                temp += 1
            if (temp < len(nums)):
                nums[temp] , nums[idx] = nums[idx] , nums[temp]
                count += 1
                idx += 1
            elif (temp >= len(nums)):
                break
        return count
