class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
     


        def rec(left, right):

            if right < left:
                return 0, 0
            curr1 , nxt1 = rec(left+1 , right)
            curr2, nxt2 = rec(left, right-1)

            if nums[left] + nxt1 > nums[right] + nxt2:
                return nums[left] + nxt1, curr1
            
            return nums[right] + nxt2, curr2
        
        p , q = rec(0, len(nums) - 1)

        return p >= q 