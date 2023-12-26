class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [ ['E' for i in range(n)] for i in range(m) ]
        alls = set()

        for val in walls:
            mat[val[0]][val[1]] = 'W'
        for val in guards:
            mat[val[0]][val[1]] = 'G'
            hor, hor1 = val[1] + 1 , val[1] - 1
            ver, ver1 = val[0] + 1 , val[0] - 1
            while (True):
                count = 0
                if (hor < n and mat[val[0]][hor] not in ('G', 'W' ,'H')):
                    count += 1
                    mat[val[0]][hor] = 'H'
                    hor += 1
                if (hor1 >= 0 and mat[val[0]][hor1] not in ('H', 'G', 'W')):
                    count += 1
                    mat[val[0]][hor1] = 'H'
                    hor1 -= 1
                if (ver < m and mat[ver][val[1]] not in ('V' , 'G' , 'W')):
                    count += 1
                    mat[ver][val[1]] = 'V'
                    ver += 1
                if (ver1 >= 0 and mat[ver1][val[1]] not in ('V' , 'G' , 'W')):
                    count += 1
                    mat[ver1][val[1]] = 'V'
                    ver1 -= 1
                if (count == 0):
                    break
        count = 0
        for row in range(m):
            for col in range(n):
                if (mat[row][col] == 'E'):
                    count += 1

        return count