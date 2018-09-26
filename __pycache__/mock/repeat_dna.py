class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        lookup = {}
        res = []
        for i in range(length - 9):
            if s[i:i+10] not in lookup:
                lookup[s[i:i+10]] = 1
            else:
                lookup[s[i:i+10]] += 1
        for key in lookup:
            if lookup[key] > 1:
                res.append(key)
        return res

if __name__ == "__main__":
    solution = Solution()
    testdata = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    result = solution.findRepeatedDnaSequences(testdata)
    print(result)