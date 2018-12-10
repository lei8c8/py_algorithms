from collections import Counter

class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        ct = Counter(A)
        for e in sorted(ct, key=abs):
            if ct[e] > ct[e*2]: 
                return False
            ct[2*e] -= ct[e]
        return True
        


s = Solution()
data = [4,-2,2,-4]
result = s.canReorderDoubled(data)
print(result)
