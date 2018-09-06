class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ''
        if not strs:
            return answer
        min_len = len(min(strs, key=lambda item: len(item)))
        for i in range(min_len):
            valid = True
            j = 0
            while j < len(strs) - 1:
                if strs[j][i] == strs[j+1][i]:
                    j += 1
                    continue
                else:
                    valid = False
                    break
            if valid:
                answer += strs[j][i]
            else:
                break
        return answer

if __name__ == "__main__":
    solution = Solution()
    testdata = ["flower","flow","flight"]
    result = solution.longestCommonPrefix(testdata)
    print(result)