class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lastocc = {}
        res = []
        for i, c in enumerate(s):
            lastocc[c] = i
        end, start = 0, 0
        for i, c in enumerate(s):
            end = max(end, lastocc[c])
            start += 1
            if (i == end):
                res.append(start)
                start = 0
        return res