class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
        else:
            return nums1[len(nums1) // 2]

if __name__ == "__main__":
    solution = Solution()
    testdata1 = [1, 2]
    testdata2 = [3, 4]
    result = solution.findMedianSortedArrays(testdata1, testdata2)
    print(result)