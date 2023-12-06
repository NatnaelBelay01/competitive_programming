class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_idx , second_idx = 0, n
        length = 2 * n
        ans = [0] * (length)
        for i in range(0, length,2):
            ans[i] = nums[first_idx]
            ans[i+1] = nums[second_idx]
            first_idx += 1
            second_idx += 1

        return ans