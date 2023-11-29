class Solution:
    def isPalindrome(self, x: int) -> bool:
        cop = x
        check = 0
        while(cop > 0):
            check *= 10
            check += cop % 10
            cop //= 10
        return x == check