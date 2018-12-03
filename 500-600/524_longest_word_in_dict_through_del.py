class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        candidates, candidatesWithLongestLen = [], []
        for element in d:
            if self.matchCondition(s, element):
                candidates.append(element)
        if len(candidates) == 0: return ""
        candidates.sort(key=len, reverse=True)
        expectedLenghth = len(candidates[0])
        candidatesWithLongestLen.append(candidates[0])
        for i in range(1, len(candidates)):
            if len(candidates[i]) == expectedLenghth:
                candidatesWithLongestLen.append(candidates[i])
        candidatesWithLongestLen.sort()
        return candidatesWithLongestLen[0]


    def matchCondition(self, s, e):
        i = 0
        if len(s) == "": return False
        for j in range(len(e)):
            while s[i] != e[j] and i < len(s):
                i += 1
                if i == len(s): 
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "abpcplea"
    d = ["ale","apple","monkey","plea"]
    result = solution.findLongestWord(s, d)
    print(result)