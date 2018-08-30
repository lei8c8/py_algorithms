class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                stack.append(c)
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                s_list[i] = stack.pop()
        return ''.join(s_list)

if __name__ == '__main__':
    solution = Solution()
    test_data = "leetcode"
    print(solution.reverseVowels(test_data))