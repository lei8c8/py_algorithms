class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.upper() == word or word.lower() == word or word.capitalize() == word

if __name__ == '__main__':
    solution = Solution()
    print(solution.detectCapitalUse('FlaG'))