class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if(len(s) == 0):
            return(s)

        temp = s.pop()
        self.reverseString(s)
        s.insert(0 , temp)
        return s