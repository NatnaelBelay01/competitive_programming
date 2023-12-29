class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        store = {}
        for idx in range(len(lst)):
            val = lst[idx][:-1]
            store[val] = lst[idx][-1]
            lst[idx] = val

        lst.sort(key=lambda x:store[x])
        return " ".join(lst)