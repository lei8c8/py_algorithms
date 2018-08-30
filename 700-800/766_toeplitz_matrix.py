class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        my_dict = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if str(r-c) not in my_dict:
                    my_dict[str(r-c)] = val
                elif my_dict[str(r-c)] != val:
                    return False
        return True


