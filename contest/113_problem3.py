class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        res = [None] * len(deck)
        i = j = 0
        while i < len(deck) and j < len(deck):
            res[j] = deck[i]
            j += 2
            i += 1
        mid = len(deck) // 2   
        res[mid] =  deck[i]
        left = mid - 2
        right = mid + 2
        i += 1
        while left > 0 and right < len(deck) -1:
            res[left] = deck[i]
            res[right] = deck[i+1]
            left -= 2
            right += 2
            i += 2
        return res
        

s = Solution()
data = [17,13,11,2,3,5,7]
result = s.deckRevealedIncreasing(data)
print(result)

