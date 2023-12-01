class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        count = 0
        total = 0
        for i in range(1, len(salary) - 1):
            total += salary[i]
            count += 1
        return total / count