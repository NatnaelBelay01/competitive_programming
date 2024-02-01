class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hashh = {}
        hashh[0] = 1
        for i in range(n):
            nums[i] = nums[i] % 2
        ans = 0
        presum = 0
        for i in range(n):
            presum += nums[i]
            ans += hashh.get(presum - k, 0)
            hashh[presum] = 1 + hashh.get(presum, 0)
        return ans