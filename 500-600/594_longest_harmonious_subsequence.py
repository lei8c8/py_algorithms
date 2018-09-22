from collections import Counter

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        ct = Counter(nums)
        elements = sorted(list(set(nums)))
        for i in range(len(elements) - 1):
            if elements[i + 1] - elements[i] > 1:
                continue
            else:
                res = max(ct[elements[i + 1]] + ct[elements[i]], res)
        return res

if __name__ == "__main__":
    solution = Solution()
    testdata = [1,4,1,3,1,-14,1,-13]
    result = solution.findLHS(testdata)
    print(result)