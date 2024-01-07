class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = {}
        for idx in range(len(nums)):

            store = {}
            check = -1 * nums[idx]
            for idx2 in range(idx+1 ,len(nums)):

                if (nums[idx2] in store):
                    temp = []
                    temp.append(-1*check)
                    temp.append(store[nums[idx2]])
                    temp.append(nums[idx2])
                    temp.sort()
                    result[tuple(temp)] = 1 + result.get(tuple(temp) , 0)
                store[check - nums[idx2]] = nums[idx2]
        return [i for i in result]