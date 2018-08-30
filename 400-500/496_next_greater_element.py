class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        positon = {}
        res = []
        for k, v in enumerate(nums2):
            positon[v] = k
        for element in nums1:
            found = False
            for element_num2 in nums2[positon[element] + 1:]:
                if element_num2 > element:
                    res.append(element_num2)
                    found = True
                    break
            if not found:
                res.append(-1)
        return res

if __name__ == '__main__':
    solution = Solution()
    test = solution.nextGreaterElement([4,1,2],[1,3,4,2])
    print(test)