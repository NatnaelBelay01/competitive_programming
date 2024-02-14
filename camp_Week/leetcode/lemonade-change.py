class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        


        countF = 0
        countT = 0

        idx = 0

        while(idx < len(bills) ):
            if(bills[idx] == 5):
                countF += 1

            elif(countF >= 1 and bills[idx] == 10):
                countT += 1
                countF -= 1
            elif( ( (countF >= 1 and countT >= 1) or countF >= 3 ) and bills[idx] == 20):
                print('hey')
                print(countF)
                if(countT >= 1):
                    countT -= 1
                    countF -= 1
                else:
                    countF -= 3
            else:
                return False
            idx += 1


        return True