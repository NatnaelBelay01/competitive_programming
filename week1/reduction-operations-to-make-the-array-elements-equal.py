class Solution:
    def reductionOperations(self, nums: List[int]) -> int:


        freq = Counter(nums)

        store = sorted(list(set(nums)))

        result = 0

        for idx in range(len(store)):
            result += idx * freq[store[idx]]
        
        return result