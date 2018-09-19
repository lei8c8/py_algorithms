class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sorted_dict = sorted(dict, key=len)
        sentence = sentence.split()
        for i in range(len(sentence)):
            for w in sorted_dict:
                if sentence[i].startswith(w):
                    sentence[i] =w
                    break
        return ' '.join(sentence)


if __name__ == "__main__":
    solution = Solution()
    testdata1 = ["cat", "bat", "rat"]
    testdata2 = "the cattle was rattled by the battery"
    result = solution.replaceWords(testdata1, testdata2)
    print(result)