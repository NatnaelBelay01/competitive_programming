class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []

        for char in s:
            if(char.isalpha() or char.isdigit()):
                check.append(char.lower())
        
        i, j = 0 , len(check) - 1

        while(i < j):
            if (check[i] != check[j]):
                return False
            i += 1
            j -= 1
        return True
        