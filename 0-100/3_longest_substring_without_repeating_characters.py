class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        lookup = {}
        left_poiter = 0
        for right_pointer in range(len(s)):
            if s[right_pointer] in lookup:
                left_poiter = max(lookup[s[right_pointer]] + 1, left_poiter)
            lookup[s[right_pointer]] = right_pointer
            max_len = max(max_len, right_pointer - left_poiter + 1)
        return max_len
                
            