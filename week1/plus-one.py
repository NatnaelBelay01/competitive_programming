class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        dig = 1
        for idx in range(len(digits) - 1, -1, -1):
            if (digits[idx] == 9):
                digits[idx] = 0
                dig = 1
            else:
                digits[idx] += dig
                dig = 0
                break
        if (dig):
            digits.insert(0,1)
        return digits
