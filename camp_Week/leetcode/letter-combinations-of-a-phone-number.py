class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        store = {"2" : ['a', 'b' , 'c'], "3":['d', 'e', 'f'], "4":['g' , 'h', 'i'], "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r' , 's'], "8":['t', 'u', 'v'] , "9":['w', 'x', 'y', 'z']}
        self.ans = []

        def rec(path, i):

            if len(path) == len(digits) :

                self.ans.append("".join(path[:]))
            if len(path) > len(digits):
                return
            if path and path[0] not in store[digits[0]]:
                return


            for k in range(i , len(digits)):
                print(k)
                for j in range(len(store[digits[k]])):
                    path.append(store[digits[k]][j])
                    rec(path , k+1)
                    path.pop()

        rec([], 0)
        return self.ans