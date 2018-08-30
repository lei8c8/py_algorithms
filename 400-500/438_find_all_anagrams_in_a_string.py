from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        counter_p = Counter(p)
        counter_s = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            counter_s[s[i]] += 1
            if counter_p == counter_s:
                res.append(i + 1 - len(p))
            counter_s[s[i + 1 - len(p)]] -= 1
            if counter_s[s[i + 1 - len(p)]] == 0:
                del counter_s[s[i + 1 - len(p)]] 
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("aecbabedce", 'a'))