class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = set()
        for interval in ranges:
            for val in range(interval[0], interval[1]+1):
                check.add(val)
        for val in range(left, right+1):
            if val not in check:
                return False
        return True
        