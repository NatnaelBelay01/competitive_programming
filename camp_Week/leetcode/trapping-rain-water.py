class Solution:
    def trap(self, height: List[int]) -> int:
        

        maxLeft = []
        maxRight = []

        val = 0
        for i in range(len(height)):
            maxLeft.append(val)
            val = max(val, height[i])

        val = 0
        for i in range(len(height)-1, -1, -1):
            maxRight.append(val)
            val = max(val, height[i])
        maxRight.reverse()
        print(maxLeft, maxRight)
        ans = 0
        for i in range(len(height)):
            temp =  min(maxRight[i], maxLeft[i]) - height[i]
            if temp > 0:
                print(temp)
                ans += temp
        return ans