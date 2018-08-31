class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = S.split()
        target_list = []
        for i in range(len(s_list)):
            if s_list[i][0] in vowels:
                temp = s_list[i] + "ma" + 'a' * (i + 1)
            else:
                temp = s_list[i][1:] + s_list[i][0] + "ma" + 'a' * (i + 1)
            target_list.append(temp)
        return ' '.join(target_list)

if __name__ == "__main__":
    solution = Solution()
    testdata = "I speak Goat Latin"
    result = solution.toGoatLatin(testdata)
    print(result)