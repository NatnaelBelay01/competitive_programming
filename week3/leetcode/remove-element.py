class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first , last = 0 , len(nums) - 1



        if(len(nums) == 0):
            return 0
        while(first < last):
            if(nums[first] == val):
                nums[first] , nums[last] = nums[last] , nums[first]
                last -= 1
            else:
                first += 1
        return last + 1 if nums[last] != val else last