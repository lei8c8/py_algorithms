class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for element in nums:
            if element in seen:
                return element
            else:
                seen.add(element)
