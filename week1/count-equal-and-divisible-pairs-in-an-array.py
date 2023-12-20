class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        count = 0


        for idx in range(len(nums)):
            for idx2 in range(idx + 1, len(nums)):
                if (idx * idx2) % k == 0 and nums[idx] == nums[idx2]:
                    count += 1
        return count