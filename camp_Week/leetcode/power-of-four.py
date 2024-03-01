class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n == 0):
            return False
        if( n == 1 or n / 4 == 1.0):
            return True
        elif(n % 4 != 0):
            return False
        temp = self.isPowerOfFour(n // 4)
        return temp
        