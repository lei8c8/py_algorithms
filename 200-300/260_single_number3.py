class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lookup = set()
        for element in nums:
            if element not in lookup:
                lookup.add(element)
            else:
                lookup.remove(element)
        return list(lookup)