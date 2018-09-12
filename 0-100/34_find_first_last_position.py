class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        position = self.binSearch(nums, target)
        if position == -1:
            return [-1, -1]
        left = right = position
        while left >= 1:
            if nums[left-1] == target:
                left -= 1
            else:
                break
        while right <= len(nums) - 2:
            if nums[right+1] == target:
                right += 1
            else:
                break
        return [left, right]
        
    def binSearch(self, nums, target):
        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        return -1