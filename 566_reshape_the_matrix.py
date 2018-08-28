from collections import deque
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row_number = len(nums)
        column_number = len(nums[0])
        res = []
        if r * c != row_number * column_number:
            return nums
        one_dim = deque([])
        for i in range(row_number):
            one_dim.extend(nums[i])
        for i in range(r):
            one_row = []
            for _ in range(c):
                one_row.append(one_dim.popleft())
            res.append(one_row)
        return res

if __name__ == '__main__':
    solution = Solution()
    testdata = [[1,2],[3,4],[5,6],[7,8]]
    print(solution.matrixReshape(testdata, 2, 4))