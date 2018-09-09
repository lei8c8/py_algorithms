from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = Counter(nums)
        degree = ct.most_common(1)[0][1]
        if degree == 1:
            return 1
        lookup = []
        for item in ct:
            if ct[item] == degree:
                lookup.append(item)
        result = len(nums)
        for element in lookup:
            left, right = 0, 0
            for i in range(len(nums)):
                if nums[i] == element:
                    left = i
                    break
            i = len(nums) - 1
            while i >= 0:
                if nums[i] == element:
                    right = i
                    break
                i -= 1
            result = min(result, right - left + 1)
        return result 