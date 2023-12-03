class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l = max(len(num1), len(num2))
        n1, n2 = 0, 0
        for i in range(l):
            if i < len(num1):
                n1 *= 10
                n1 += ord(num1[i]) - 48
            if i < len(num2):
                n2 *= 10
                n2 += ord(num2[i]) - 48
        return str(n1 * n2)