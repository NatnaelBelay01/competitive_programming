class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        check = {}
        tot = 0

        left = 0
        ans = 0

        for right in range(len(nums)):

            tot += nums[right]

            check[nums[right]] = 1 + check.get(nums[right] , 0)

            while(len(check) < right - left + 1):
                tot -= nums[left]
                check[nums[left]] -= 1
                if(check[nums[left]] == 0):
                    check.pop(nums[left])
                left += 1
            
            ans = max(ans , tot)
        return ans
        