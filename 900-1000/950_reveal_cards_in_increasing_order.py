from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        deck, queue = deque(deck), deque([i for i in range(len(deck))])
        res = [None] * len(deck)
        while queue:
            res[queue.popleft()] = deck.popleft()
            if queue: queue.append(queue.popleft())
        return res