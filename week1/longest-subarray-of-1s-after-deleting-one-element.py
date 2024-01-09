class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        check = {}
        check[0] = 0
        check[1] = 0
        result = 0

        left = 0

        for right in range(len(nums)):
            
            check[nums[right]] = 1 + check.get(nums[right])

            while(check[0] > 1):
                check[nums[left]] -= 1
                left += 1
            
            temp = check[1] if (check[0] == 1 ) else check[1] - 1 
            
            result = max(result , temp)

        return result
            
            

