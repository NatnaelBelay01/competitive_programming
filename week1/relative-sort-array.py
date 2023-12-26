class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        pos = 0

        for val in arr2:
            for idx in range(len(arr1)):
                if (arr1[idx] == val):
                    arr1[pos] , arr1[idx] = arr1[idx], arr1[pos]
                    pos += 1

        for idx in range(pos + 1, len(arr1)):
            temp = idx
            while (temp > pos and arr1[temp] < arr1[temp - 1]):
                arr1[temp] , arr1[temp - 1] = arr1[temp - 1] , arr1[temp]
                temp -= 1
        
        return arr1