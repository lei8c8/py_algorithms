from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        ct = Counter(nums1)
        for element in nums2:
            if element in ct:
                res.append(element)
                ct[element] -= 1
                if ct[element] == 0:
                    del ct[element]
        return res
        