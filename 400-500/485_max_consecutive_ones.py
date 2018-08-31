class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target_max = 0
        temp_max = 0
        for element in nums:
            if element == 1:
                temp_max += 1
            else:
                target_max = max(target_max, temp_max)
                temp_max = 0
        target_max = max(target_max, temp_max)
        return target_max

if __name__ == "__main__":
    solution = Solution()
    testdata = [1]
    result = solution.findMaxConsecutiveOnes(testdata)
    print(result)