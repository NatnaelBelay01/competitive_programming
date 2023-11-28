class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        marea = 0
        fro = 0
        bak = len(height) - 1
        while (fro < bak):
            if (height[fro] < height[bak]):
                area = height[fro] * (bak - fro)
            else:
                area = height[bak] * (bak - fro)
            marea = max(marea, area)
            if (height[fro] < height[bak]):
                fro += 1
            else:
                bak -= 1
        return marea