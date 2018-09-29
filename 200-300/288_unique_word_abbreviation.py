
from collections import defaultdict
class ValidWordAbbr:

    def __init__(self, dictionary):
        self.seen = defaultdict(set)
        for word in dictionary:
            self.seen[self.to_abbr(word)].add(word)
       
    def to_abbr(self, word):
        if len(word) <= 2: return word  
        return word[0] + str(len(word[1:-1])) + word[-1]

    def isUnique(self, word):
        abbr = self.to_abbr(word)
        if abbr not in self.seen:
            return True
        return word in self.seen[abbr] and len(self.seen[abbr]) == 1