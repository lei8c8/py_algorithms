class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res, lookup = "", set(words)
        for word in words:
            if len(word) > len(res) or (len(word) == len(res) and word < res):
                satisfy = True
                i = 1
                while i < len(word):
                    if word[:i] not in lookup:
                        satisfy = False
                        break
                    i += 1
                if satisfy: res = word
        return res