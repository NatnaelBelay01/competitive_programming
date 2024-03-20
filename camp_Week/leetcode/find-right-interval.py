class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        start = []
        end = []
        store = {}
        for idx, val in enumerate(intervals):
            start.append(val[0])
            end.append(val[1])
            store[val[0]] = idx
        
        start.sort()
        ans = []

        for target in end:

            l = -1
            r = len(start)

            while(r > l + 1):
                
                m = (l + r) // 2

                if start[m] < target:
                    l = m
                else:
                    r = m
            if r < len(start):
                ans.append(store[start[r]])
            else:
                ans.append(-1)
        
        return ans

