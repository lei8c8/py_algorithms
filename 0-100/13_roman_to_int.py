class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        i = 0
        hash_table = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        while i < len(s) - 1:
            if hash_table[s[i+1]] > hash_table[s[i]]:
                answer += (hash_table[s[i+1]] - hash_table[s[i]])
                i += 2
            else:
                answer += hash_table[s[i]]
                i += 1
        if i == len(s) - 1:
            answer += hash_table[s[-1]]
        return answer