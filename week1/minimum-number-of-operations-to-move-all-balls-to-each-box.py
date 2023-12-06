class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        total = 0
        ans = []
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if (i != j and boxes[j] == '1'):
                    total += abs(i-j)
            ans.append(total)
            total = 0
        return ans