class Solution:
 
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        store = {}
        flag = 0
        for idx, val in enumerate(order):
            store[val] = idx + 1
        for i in range(1, len(words)):

            for j in range(len(words[i])):
                if (j >= len(words[i-1])):
                    break
                if (store[words[i-1][j]] < store[words[i][j]]):
                    flag = 1
                    break
                elif (store[words[i-1][j]] > store[words[i][j]]):
                    return False
            if (len(words[i-1]) > len(words[i]) and flag == 0):
                return False
            flag = 0

        return True