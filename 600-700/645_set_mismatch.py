from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ct = Counter(nums)
        lookup_hash_table = set(list(range(1,len(nums) + 1)))
        duplicated_item = ct.most_common(1)[0][0]
        return [duplicated_item, (lookup_hash_table - set(nums)).pop()]

if __name__ == "__main__":
    solution = Solution()
    test_data = [1,2,2,4]
    test_result = solution.findErrorNums(test_data)
    print(test_result)
