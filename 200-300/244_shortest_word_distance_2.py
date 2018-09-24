class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.length = len(words)
        self.lookup = self._hashIt(words)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_distance = self.length
        for i in self.lookup[word1]:
            for j in self.lookup[word2]:
                min_distance = min(min_distance, abs(j - i))
        return min_distance

    def _hashIt(self, words):
        lookup = {}
        for i, v in enumerate(words):
            if v not in lookup:
                lookup[v] = {i}
            else:
                lookup[v].add(i)
        return lookup