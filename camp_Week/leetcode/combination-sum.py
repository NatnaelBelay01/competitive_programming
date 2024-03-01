class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.ans = []


        def rec(path, i):

            if sum(path) == target:
                self.ans.append(path[:])

                #the base-case
            
            if sum(path) > target:
                return
 
            
            
            for j in range(i , len(nums)):

                path.append(nums[j])
                rec(path, j)
                path.pop()
        
        rec([] , 0)
        return self.ans