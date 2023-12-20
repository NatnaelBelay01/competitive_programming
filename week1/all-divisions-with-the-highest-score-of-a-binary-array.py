class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        zeros = {}
        zeros[0] = 0
        ones = {}
        ones[len(nums)] = 0
        for idx , val in enumerate(nums):
            count = 1 if val == 0 else 0
            zeros[idx + 1] = count + zeros[idx]
        
        for idx in range(len(nums) - 1, -1, -1):
            count = 1 if nums[idx] == 1 else 0
            ones[idx] = count + ones[idx+1]

        for idx in zeros:
            zeros[idx] += ones[idx]
 
        result = []

        max_sum = 0
        for idx in zeros:
            if (max_sum < zeros[idx]):
                max_sum = zeros[idx]
                result = []
                result.append(idx)
            elif (max_sum == zeros[idx]):
                result.append(idx)
        return result
