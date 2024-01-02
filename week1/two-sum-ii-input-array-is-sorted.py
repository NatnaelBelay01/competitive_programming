class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1

        while (last > first):
            if (numbers[last] + numbers[first] > target):
                last -= 1
            elif (numbers[last] + numbers[first] < target):
                first += 1
            else:
                result = []
                result.append(first + 1)
                result.append(last + 1)
                return result
