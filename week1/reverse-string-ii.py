class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        lst = list(s)
        while (i < len(s)):
            lst[i:i+k] = lst[i:i+k][::-1]
            i += 2*k
        return "".join(lst)