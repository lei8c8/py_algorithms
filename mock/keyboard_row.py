class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lookup1 = set(['q','w','e','r','t','y','u','i','o','p'])
        lookup2 = set(['a','s','d','f','g','h','j','k','l'])
        lookup3 = set(['z','x','c','v','b','n','m'])
        res = []
        for word in words:
            if self.all_in_set(lookup1, word):
                res.append(word)
            if self.all_in_set(lookup2, word):
                res.append(word)
            if self.all_in_set(lookup3, word):
                res.append(word)
        return res
    
    def all_in_set(self, set_ch, w):
        for c in w:
            if c.lower() not in set_ch:
                return False
        return True

