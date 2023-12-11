class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        for val in nums:
            store.add(val)
        count, count1 = 0 , 1
        for val in nums:
            if(val - 1 not in store ):
                count1 = 1
                temp = val + 1
                while (temp in store):
                    count1 += 1
                    temp += 1
            count = max(count1, count)
        return count