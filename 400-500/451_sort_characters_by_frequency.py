from collections import Counter

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ct = Counter(s)
        my_list = []
        for element in ct.most_common():
            my_list.append(element[0] * element[1])
        return ''.join(my_list)

if __name__ == "__main__":
    solution = Solution()
    test_data = "tree"
    result = solution.frequencySort(test_data)
    print(result)
