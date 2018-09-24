class Solution:
    def shortestDistance(self, words, word1, word2):
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
        for i in lookup[word1]:
            for j in lookup[word2]:
                min_distance = min(min_distance, abs(j - i))
        return min_distance

if __name__ == "__main__":
    solution = Solution()
    result = solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "practice")
    print(result)
