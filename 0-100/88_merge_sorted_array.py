class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        start_1 = m - 1
        start_2 = n - 1
        insert_point = m + n - 1 
        while start_1 >= 0 and start_2 >= 0:
            if nums1[start_1] >= nums2[start_2]:
                nums1[insert_point] = nums1[start_1] 
                start_1 -= 1
            else:
                nums1[insert_point] = nums2[start_2]
                start_2 -= 1
            insert_point -= 1

        if start_1 >= 0:
            while start_1 >= 0:
                nums1[insert_point] = nums1[start_1] 
                start_1 -= 1
                insert_point -= 1

        if start_2 >= 0:
            while start_2 >= 0:
                nums1[insert_point] = nums2[start_2]
                start_2 -= 1
                insert_point -= 1