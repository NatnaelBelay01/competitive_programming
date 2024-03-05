class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:


        if sum(nums) < target:
            return []


        nums.sort()
        res = []
        seen = set()


        #1 1 2 5 6 7 10 


        def rec(path , i):

            if sum(path) > target:
                return

            if sum(path) == target:
                if tuple(path) not in seen:
                    res.append(path[:])
                    seen.add(tuple(path[:]))
                return
            check = -1
            for idx in range(i , len(nums)):
                if check != nums[idx]:
                    path.append(nums[idx])
                    if sum(path) <= target:
                        rec(path, idx+1)
                    check = path.pop()
        
        rec([], 0)

        return res