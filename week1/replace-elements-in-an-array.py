class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store = {}
        for idx, val in enumerate(nums):
            store[val] = [val, idx]


        for operation in operations:
            old_value, new_value = operation
            temp = store[old_value][1]
            store.pop(old_value)
            store[new_value] = [new_value, temp]


        result = [0] * len(nums)

        for value in store:
            result[store[value][1]] = store[value][0]

        return result
        