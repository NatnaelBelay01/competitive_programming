class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        length = len(indices)
        ans = [' ']* length
        for i in range(length):
            ans[indices[i]] = s[i]
        return "".join(ans)