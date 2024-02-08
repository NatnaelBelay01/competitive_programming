class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        n = 0

        for val in trips:
            n = max(n, val[2])
        
        arr = [0] * (n + 1)

        for val in trips:
            arr[val[1]] += val[0]
            if(val[2] < len(arr)):
                arr[val[2]] += -1 * val[0]

        for idx in range(1 ,len(arr)):
            arr[idx] += arr[idx-1]

        print(arr)
        for val in arr:
            if(val > capacity):
                return False
        return True 