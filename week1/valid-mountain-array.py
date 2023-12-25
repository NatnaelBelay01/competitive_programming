class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = 1

        while(idx < len(arr)):
            if (arr[idx-1] == arr[idx]):
                return False

            if (arr[idx-1] > arr[idx]):
                break
            idx += 1
        
        if (idx == len(arr) or idx == 1): return False

        while(idx < len(arr)):

            if (arr[idx-1] <= arr[idx] ):
                return False
            idx += 1
        
        return True
    