class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        count = 0

        

        
       
        for val in zip(*strs):
            
            if (sorted(list(val)) != list(val)):

                count += 1
            
        return count
