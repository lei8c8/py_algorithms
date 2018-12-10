class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        chars, res = "abcdefghijklmnopqrstuvwxyz", []
        myDict = dict(zip(list(order), list(chars)))
        for word in words:
            temp = ''.join([myDict[c] for c in word])
            res.append(temp)
        return res == sorted(res)

s = Solution()
words = ["reb","inci"]
order = "tcyklqfhoeapndgbimsujzvxwr"
result = s.isAlienSorted(words, order)
print(result)
