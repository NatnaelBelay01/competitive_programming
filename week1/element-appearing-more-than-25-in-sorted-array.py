class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        occur = len(arr) / 4
        store = {}

        for val in arr:
            store[val] = 1 + store.get(val , 0)
        for val in store:
            if (store[val] > occur):
                return val