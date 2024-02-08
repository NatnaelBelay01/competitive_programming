class Solution:
    def bestClosingTime(self, customers: str) -> int:
        

        ns  = [0] * len(customers)
        ns[0] = 0 if customers[0] == 'Y' else 1
        ys =  [0] * len(customers)
        ys[-1] = 0 if customers[-1] == 'N' else 1

        idx = len(customers) - 2

        while(idx >= 0):
            if(customers[idx] == 'Y'):
                ys[idx] += 1 + ys[idx + 1]
            else:
                ys[idx] += ys[idx + 1]

            idx -= 1



        for right in range(1, len(customers)):

            if(customers[right - 1] == 'N'):
                ns[right] += 1 + ns[right - 1]
            else:
                ns[right] += ns[right - 1]
            
        ns.append(ns[-1])
        ys.append(0)

        ans = float('inf')
        idx = 0


        for right in range(len(ns)):
            if (ns[right] + ys[right] < ans):
                ans = ns[right] + ys[right]
                idx = right
        
        
        return idx
            
