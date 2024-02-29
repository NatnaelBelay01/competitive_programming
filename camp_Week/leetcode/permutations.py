class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        self.ans = []

        def rec(path, i):

            if(len(path) == len(nums) ):
                if(len(set(path)) == len(nums)):
                    self.ans.append(path[:])
                return

            for idx in range(len(nums)):
                
                path.append(nums[idx])
                rec(path, idx)
                path.pop()
        
        rec([] , 0)

        return self.ans