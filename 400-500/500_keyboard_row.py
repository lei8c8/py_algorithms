class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set(list('QWERTYUIOP'))
        set2 = set(list('ASDFGHJKL'))
        set3 = set(list('ZXCVBNM'))
        res = []
        for word in words:
            if set(list(word.upper())).issubset(set1):
                res.append(word)
            elif set(list(word.upper())).issubset(set2):
                res.append(word)
            elif set(list(word.upper())).issubset(set3):
                res.append(word)    
        return res


if __name__ == '__main__':
    solution = Solution()
    testdata = ["Hello", "Alaska", "Dad", "Peace"]
    result = solution.findWords(testdata)
    print(result)