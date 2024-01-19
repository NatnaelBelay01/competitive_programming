class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        left = 0
        total = 0
        result = float('-inf')


        for right in range(len(nums)):

            total += nums[right]

            if (right - left + 1 == k):
                result = max(result , total / k)

            elif (right - left + 1 > k):
                total -= nums[left]
                left += 1
                result = max(result , total / k)
                  
        return result