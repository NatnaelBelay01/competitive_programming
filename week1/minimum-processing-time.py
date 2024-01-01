class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
 


        processorTime.sort()
        tasks.sort()
        slowest = 0
        
        for idx in range(len(tasks)):
            slowest = max(tasks[len(tasks) - 1 - idx] + processorTime[idx//4], slowest)
        
        return slowest
        