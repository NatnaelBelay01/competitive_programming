class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()


        for ryt in range(len(nums)):
            mid = ryt + 1
            lst = len(nums) - 1

            while(mid < lst):
                temp = nums[lst] + nums[mid] + nums[ryt]
                if(abs(ans) > abs(temp - target)):
                    ans = temp - target
                if(temp > target):
                    lst -= 1
                elif(temp < target):
                    mid += 1
                else:
                    return target
        return ans + target