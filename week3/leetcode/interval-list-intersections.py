class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if firstList == [] or secondList == []:
            return []

        
        ans = []
        i = 0
        j = 0
        while(i < len(firstList) and j < len(secondList)):
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])

            if(left <= right):
                ans.append([left, right])
            
            if(firstList[i][1] < secondList[j][1]):
                i += 1
            else:
                j += 1
        return ans 


        return ans
