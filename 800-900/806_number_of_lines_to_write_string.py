class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        number_of_lines = 1
        current_number = 0
        for c in S:
            c_width = widths[ord(c) - ord('a')]
            if current_number + c_width > 100:
                number_of_lines += 1
                current_number = c_width
            else:
                current_number += c_width
        return [number_of_lines, current_number]

if __name__ == '__main__':
    solution = Solution()
    test = solution.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")
    print(test)