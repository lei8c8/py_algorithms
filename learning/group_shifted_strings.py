class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        lookup, res = {}, []
        for string in strings:
            shiftedStr = self.shiftToStartingWithA(string)
            if  shiftedStr not in lookup:
                lookup[shiftedStr] = [string]
            else:
                lookup[shiftedStr].append(string)
        for key in lookup:
            res.append(lookup[key])
        return res
        
    def shiftToStartingWithA(self, s):
        res = []
        base = s[0]
        for ch in s:
            diff = ord(ch) - ord(base)
            if diff < 0:
                diff = diff + 26
            res.append(chr(diff + ord('a')))
        return ''.join(res)