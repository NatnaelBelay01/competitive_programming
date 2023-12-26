class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        temp = 0
        place = 0
        for idx in range(1 ,len(heights)):
            temp = idx
            while (temp > 0 and heights[temp] > heights[temp-1]):
                heights[temp] , heights[temp - 1] = heights[temp - 1], heights[temp]
                names[temp] , names[temp - 1] = names[temp - 1] , names[temp]
                temp -=1
        return names
        