class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        self.ans = []
  
        def rec(path, i):

            if path not in self.ans:
                self.ans.append(path[:])

                #the base case
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                rec(path, j+1)
                path.pop()
        rec([], 0)

        return list(self.ans)