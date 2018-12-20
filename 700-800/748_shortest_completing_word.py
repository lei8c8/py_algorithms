from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        res = "abcdefghijklmnopqrstuvwxyz"
        for word in words:
            ct = Counter(word)
            lp = self.createCharArray(licensePlate)
            for key in ct:
                if ct[key] >= lp[ord(key) - ord('a')]:
                    lp[ord(key) - ord('a')] = 0
                else:
                    lp[ord(key) - ord('a')] -= ct[key]
            if all(x == 0 for x in lp) and len(word) < len(res):
                res = word
        return res

    def createCharArray(self, l):
        res = [0] * 26
        for e in l:
            if e.isalpha():
                res[ord(e.lower()) - ord('a')] += 1
        return res    