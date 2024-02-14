class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        idx = len(nums) - 1

        ans = 0

        while(idx > 0):
            if(nums[idx] < nums[idx - 1]):
                sp = math.ceil(nums[idx - 1] / nums[idx])
                ans += sp - 1
                nums[idx-1] //= sp
            idx -= 1

        return ans
