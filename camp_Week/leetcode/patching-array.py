class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        check = 0

        patches = 0

        for i in nums:
            

            while i > check + 1:
                patches += 1
                check += check + 1

                if check >= n:
                    return patches
            
            check += i

            if check >= n:
                return patches
        
        while n > check:
            check += check + 1
            patches += 1
        

        return patches