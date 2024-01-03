class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        first = 0
        second = 0
        count = 0

        g.sort()
        s.sort()

        while(first < len(g) and second < len(s)):
            if(s[second] < g[first]):
                second += 1
            else:
                second += 1
                first += 1
                count += 1

        return count