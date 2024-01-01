class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        leng = len(processorTime)
        total = 4 * leng * [0]

        for idx in range(len(total)):
            total[idx] = processorTime[idx % leng]
        print(total)

        total.sort()
        tasks.sort()

        n = len(tasks) - 1
        for idx in range(len(total)):
            total[idx] += tasks[n - idx]
        
        return max(total)
        