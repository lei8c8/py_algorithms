from collections import Counter

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = Counter(nums)
        return ct.most_common(1)[0][0]