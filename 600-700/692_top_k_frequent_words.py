from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ct = Counter(words)
        ca = ct.keys()
        ca.sort(key = lambda w: (-ct[w], w))
        return ca[:k]
