class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        one , two = float('inf') , float('inf')


        for val in nums:
            if (val <= one):
                one = val
            elif (val <= two):
                two = val
            else:
                return True


        return False