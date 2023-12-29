class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if (num == 0):
            return 0
        flag = False
        if (num < 0):
            num *= -1
            flag = True
        lst = list(str(num))

        if(flag):
            lst.sort(reverse=True)
            return -1 * int("".join(lst))

        lst.sort()
        if(lst[0] == '0'):
            idx = 0
            while (idx < len(lst) and lst[idx] == '0'):
                idx += 1
            lst[idx] , lst[0] = lst[0], lst[idx]

        return int("".join(lst))