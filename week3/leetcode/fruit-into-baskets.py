class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        basket = {}
        left = 0
        ans = 0
        for right in range(len(fruits)):
            basket[fruits[right]] = 1 + basket.get(fruits[right], 0)
            while(len(basket) > 2):
                basket[fruits[left]] -= 1
                if(basket[fruits[left]] == 0):
                    basket.pop(fruits[left])
                left += 1
            ans = max(ans , right - left + 1)
        return ans
        