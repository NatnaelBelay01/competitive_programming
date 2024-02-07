class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        res = [0] * (n)

        for val in bookings:
            res[val[0] - 1] += val[2]
            if(val[1] < len(res)):
                res[val[1]] -= val[2]
        
        print(res)
        
        for idx in range(1, len(res)):
            res[idx] += res[idx - 1]
        
        return res


        