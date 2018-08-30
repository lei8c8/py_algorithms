from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ct = Counter(nums)
        criteria = len(nums) / 3
        res = []
        for k in ct:
            if ct[k] > criteria:
                res.append(k)
        return res

if __name__ == '__main__':
    solution = Solution()
    test_data = [1,1,1,3,3,2,2,2]
    test_result = solution.majorityElement(test_data)
    print(test_result)
