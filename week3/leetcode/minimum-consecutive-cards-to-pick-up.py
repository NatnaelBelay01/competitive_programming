class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        left = 0

        check = {}

        for right in range(len(cards)):

            check[cards[right]] = 1 + check.get(cards[right], 0)

            while(len(check) < right - left + 1):
                ans = min(ans , right - left + 1)
                check[cards[left]] -= 1
                if(check[cards[left]] == 0):
                    check.pop(cards[left])
                left += 1
        if(ans == float('inf')):
            return -1
        return ans
            
