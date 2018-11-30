class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for w in dict:
            if len(w) not in self.lookup:
                self.lookup[len(w)] = [w]
            else:
                self.lookup[len(w)].append(w)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.lookup: return False
        for e in self.lookup[len(word)]:
            cnt = 0
            for i in range(len(word)):
                if word[i] != e[i]:
                    cnt += 1
                    if cnt >= 2: break
            if cnt == 1: return True
        return False
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)