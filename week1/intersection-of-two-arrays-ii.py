class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check1 = {}
        for val in nums1:
            check1[val] = 1 + check1.get(val , 0)
        
        check2 = {}
        for val in nums2:
            check2[val] = 1 + check2.get(val , 0)
        
        result = []
        for val in check1:
            if(val in check2):
                num = min(check2[val] , check1[val])
                for i in range(num):
                    result.append(val)
        
        return result