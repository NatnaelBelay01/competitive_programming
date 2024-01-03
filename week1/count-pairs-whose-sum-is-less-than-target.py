class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        


        count = 0



        for idx in range(len(nums)):
            for idx2 in range(idx + 1 ,len(nums)):
                if (nums[idx] + nums[idx2] < target):
                    count += 1
            



    
        return count