class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        
        deck.sort(reverse=True)
        queue = deque([deck[0]])

        for i in range(1, len(deck)):
            b = queue.pop()
            queue.appendleft(b)
            queue.appendleft(deck[i])
        
        return list(queue)