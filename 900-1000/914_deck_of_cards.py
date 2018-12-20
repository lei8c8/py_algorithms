from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        ct, length = Counter(deck), len(deck)
        for i in range(2, length + 1):
            if length % i == 0:
                if all(x % i == 0 for x in ct.values()):
                    return True
        return False