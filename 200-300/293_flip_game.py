class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or '++' not in s:
            return []
        
        res = []
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                res.append(s[:i] + '--' + s[i+2:])
        
        return res