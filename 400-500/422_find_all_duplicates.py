class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lookup = {}
        res = []
        for element in nums:
            if element not in lookup:
                lookup[element] = 1
            else:
                res.append(element)
        return res
        