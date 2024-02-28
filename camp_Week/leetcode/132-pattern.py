class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        check = nums[0]

        for idx in range(1 , len(nums)):

            while(stack and nums[idx] >= stack[-1][0]):
                stack.pop()
            
            if( stack and nums[idx] > stack[-1][1]):
                return True
            stack.append([nums[idx], check])
            check = min(nums[idx], check)
        
        return False