class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        r = len(letters)
        l = -1

        while(r > l + 1):
            
            mid = (r + l) // 2
            
            if letters[mid] >  target:
                r = mid
            else:
                l = mid
        
        return letters[r] if r < len(letters) else letters[0]