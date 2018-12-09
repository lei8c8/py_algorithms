class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
       
        str2 = [i for i in ' '.join((''.join(str)).split()[::-1])]
        for i in range(len(str2)):
            str[i] = str2[i]