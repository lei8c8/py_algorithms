from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ct_s = Counter(s)
        ct_t = Counter(t)
        ct1 = ct_s - ct_t
        ct2 = ct_t - ct_s
        return len(ct1.items()) == 0 and len(ct2.items()) == 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.isAnagram("anargam", "nagaram")
    print(result)
        