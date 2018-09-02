from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ct = Counter(magazine)
        for element in ransomNote:
            if not element in ct:
                return False
            else:
                if ct[element] == 0:
                    return False
                else:
                    ct[element] -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    result = solution.canConstruct("aa", "ab")
    print(result)