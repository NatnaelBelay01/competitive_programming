class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        def rec(path, i):

            if (path):
                self.ans.append(path[:])

            
            for j in range(i, len(nums)):
                path.append(nums[j])
                rec(path , j+1)
                path.pop()
        rec([] , 0)
        self.ans.append([])
        return self.ans