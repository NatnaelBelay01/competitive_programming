class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            l = 0
            m = len(left)
            n = len(right)
            r = 0
            ans = []
            while(l < m or r < n):

                if (l < m and r < n):
                    if (left[l] > right[r]):
                        ans.append(right[r])
                        r += 1
                    else:
                        ans.append(left[l])
                        l += 1
                else:
                    if l >= m:
                        ans.append(right[r])
                        r += 1
                    else:
                        ans.append(left[l])
                        l += 1
            return ans
        def mergeSort(num, l , r):
            

            if( r == l + 1 or r == l):
                return [num[l]]
            mid = (l + r ) // 2

            left = mergeSort(num, l , mid)
            right = mergeSort(num, mid, r)
            return merge(left, right)


        return mergeSort(nums, 0, len(nums) )