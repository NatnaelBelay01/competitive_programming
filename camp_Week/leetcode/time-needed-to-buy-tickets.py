class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        nums = deque([i for i in range(len(tickets))])


        count = 0

        while(nums):
            for i in range(len(nums)):
                idx = nums.popleft()
                tickets[idx] -= 1
                if tickets[idx] > 0:
                    nums.append(idx)
                count += 1
                
                if tickets[k] == 0:
                    return count

        
