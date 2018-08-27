from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        return (Counter(t) - Counter(s)).popitem()[0]

