class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        store = {}

        for idx , val in enumerate(nums):
            if val not in store:
                store[val] = []
            store[val].append(idx)
        
        print(store)
        res = [0] * len(nums)

        for val in store:
            

            if( len(store[val]) == 1):
                res[store[val][0]] = 0
                continue
            presum = 0
            pos = 0
            sursum = sum(store[val])
            s = len(store[val])
            for idx , i in enumerate(store[val]):
                presum += i
                sursum -= i
                pos += 1
                s -= 1
                res[i] = ((pos * i) - presum) + (sursum - (s*i)) 


        return res