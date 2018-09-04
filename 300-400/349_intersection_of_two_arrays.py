class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        for element in set2:
            if element in set1:
                res.append(element)
        return res
