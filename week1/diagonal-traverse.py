class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        check = {}

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if(row + col not in check):
                    check[row + col] = []
                check[row + col].append(mat[row][col])
        for val in check:
            if (val % 2 == 0):
                check[val].reverse()

        result = []
        num = 0
        while(num in check):
            result += check[num]
            num += 1
        return result