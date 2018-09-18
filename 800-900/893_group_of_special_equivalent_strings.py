class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        lookup = set()
        for s in A:
            s = list(s)
            s1, s2 = s[::2], s[1::2]
            s1, s2 = sorted(s1), sorted(s2)
            lookup.add((''.join(s1), ''.join(s2)))
        return len(lookup)    