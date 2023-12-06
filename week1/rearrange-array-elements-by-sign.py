class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        positive = []
        negative = []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        length = len(positive)
        idx = 0
        while idx < length:
            ans.append(positive[idx])
            ans.append(negative[idx])
            idx += 1
        return ans