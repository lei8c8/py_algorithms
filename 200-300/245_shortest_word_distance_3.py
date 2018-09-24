class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_distance, lookup = len(words), {}
        for i, v in enumerate(words):
            if v not in lookup:
                lookup[v] = {i}
            else:
                lookup[v].add(i)
        if word1 != word2:
            for i in lookup[word1]:
                for j in lookup[word2]:
                    min_distance = min(min_distance, abs(j - i))
        else:
            indexes = list(lookup[word1])
            indexes.sort()
            for i in range(len(indexes) - 1):
                min_distance = min(min_distance, indexes[i + 1] - indexes[i])
        return min_distance
        