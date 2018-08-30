class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_hash_map = {}
        for i in nums:
            if i not in my_hash_map:
                my_hash_map[i] = 1
            else:
                return True
        return False
