class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for k, v in enumerate(numbers):
            mydict[v] = k
        for i in range(len(numbers)):
            if (target - numbers[i]) in mydict:
                return [i + 1, mydict[target - numbers[i]] + 1]


if __name__ == '__main__':
    solution = Solution()
    test_result = solution.twoSum([2,7,11,15], 9)
    print(test_result)