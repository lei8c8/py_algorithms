class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_list = []
        for c in s:
            if c.isalnum():
                temp_list.append(c.lower())
        return temp_list == temp_list[::-1]