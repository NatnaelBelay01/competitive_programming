class Solution:
    def freqAlphabets(self, s: str) -> str:
        lst = list()
        i = len(s) - 1
        while (i >= 0):
            if (s[i] == '#'):
                lst.append(chr(ord('a') - 1 + int(s[i-2] + s[i-1])))
                i -= 3
            else:
                lst.append(chr(ord('a') - 1 + int(s[i])))
                i -= 1
        lst.reverse()
        print(lst)
        return "".join(lst)