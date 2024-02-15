class Solution:
    def longestPalindrome(self, s: str) -> int:

        store = Counter(s)
        res = 0
        odd = 0

        print(store)
        for val in store:
            if store[val] % 2 == 1:
                odd = 1
                res += store[val] - 1

            elif store[val] % 2 == 0:
                res += store[val]
        if(odd):
            return res + 1
        return res
        