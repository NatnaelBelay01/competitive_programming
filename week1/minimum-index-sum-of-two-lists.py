class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        hash_map = {}
        least_idx_sum = float('inf')
        for idx, word in enumerate(list1):
            if word in list2:
                hash_map[word] = idx
        for idx, word in enumerate(list2):
            if word in hash_map:
                hash_map[word] += idx
        for val in hash_map:
            if(hash_map[val] < least_idx_sum):
                least_idx_sum = hash_map[val]
                ans = []
                ans.append(val)
            elif(hash_map[val] == least_idx_sum):
                ans.append(val)
        return ans