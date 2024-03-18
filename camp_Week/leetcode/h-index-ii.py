class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # if citations[-1] == 0:
        #     return 0
        def is_valid(n):
            count = 0
            for i in citations:
                if i >= n:
                    count += 1
            return count >= n


        r = max(len(citations)+1, citations[-1])
        l = 0

        while(r > l + 1):

            mid = (r + l) // 2

            if (is_valid(mid)):
                l = mid
            else:
                r = mid
        
        return l
        