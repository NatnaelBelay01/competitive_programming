class Solution:
    def minimizedStringLength(self, s: str) -> int:
        check = set()
        for char in s:
            check.add(char)
        return len(check)