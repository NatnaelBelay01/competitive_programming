class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        check = {}


        for idx , val in enumerate(temperatures):
            
            while(stack and val > temperatures[stack[-1]]):
                
                temp = stack.pop()
                check[temp] = idx - temp
                
            stack.append(idx)


        for idx in stack:
            check[idx] = 0
        
        ans = []
        for idx in range(len(temperatures)):
            ans.append(check[idx])
        
        return ans
        