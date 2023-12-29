class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        idx = len(arr) - 1
        result = []

        while (idx > 0):
            max_num = float('-inf')
            max_idx = -1

            for i in range(idx , -1 , -1):

                if (max_num < arr[i]):
                    
                    max_num = arr[i]
                    print(max_num)
                    max_idx = i
            
            arr[:max_idx + 1] = arr[max_idx::-1]
            print(arr)
            result.append(max_idx + 1)
            arr[:idx + 1] = arr[idx::-1]
            print(arr)
            result.append(idx + 1)
            idx -= 1
        print(arr)
        return result