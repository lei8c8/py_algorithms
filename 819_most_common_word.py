from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ignore = {"!", "?","'", ";", ".", ","}
        paragraph = ''.join(c for c in paragraph if c not in ignore)
        paragraph = paragraph.lower()
        my_list = paragraph.split()
        my_counter = Counter(my_list)
        for item in my_counter.most_common():
            if item[0] not in banned:
                return item[0]
        return None
        
if __name__ == "__main__":
    solution = Solution()
    testdata = "Bob hit a ball, the hit BALL flew far after it was hit."
    testdata2 = ["hit"]
    result = solution.mostCommonWord(testdata, testdata2)
    print(result)
