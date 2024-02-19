class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) < 2:
            return ""
        
        check = list(palindrome)
  

        for idx in range(len(check)//2):
            if(check[idx] != 'a'):
                check[idx] = 'a'
                return "".join(check)
        check[-1] = 'b'
        return "".join(check)

                
        