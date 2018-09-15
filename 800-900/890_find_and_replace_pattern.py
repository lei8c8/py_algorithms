class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def findMatch( word):
            d, w = {}, {}
            for i, j in zip(word, pattern):
                if i not in d: d[i] = j
                if j not in w: w[j] = i
                if (d[i], w[j]) != (j, i):
                    return False
            return True

        return list(filter(findMatch, words))
