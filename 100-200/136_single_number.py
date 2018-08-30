class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mySet = set()
        for item in nums:
            if item not in mySet:
                mySet.add(item)
            else:
                mySet.remove(item)
        return mySet.pop()
