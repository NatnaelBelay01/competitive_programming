class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_idx = 0
        length = len(s) + len(spaces)
        ans = [' '] * length
        for idx in range(len(spaces)):
            spaces[idx] += idx
        space = set(spaces)
        for idx in range(length):
            if idx in space:
                continue
            else:
                ans[idx] = s[s_idx]
                s_idx += 1

        return "".join(ans)