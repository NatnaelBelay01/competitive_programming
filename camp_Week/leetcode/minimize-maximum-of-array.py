class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        check = nums[0]

        for idx in range(1 , len(nums)):
            check += nums[idx]
            val = math.ceil( check / (idx + 1) )
            if(nums[idx] >  val ):
                nums[idx] = val

        return max(nums)