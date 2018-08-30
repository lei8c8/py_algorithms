class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = i
            else:
                if i - my_dict[nums[i]] <= k:
                    return True
                else:
                    my_dict[nums[i]] = i
        return False

if __name__ == '__main__':
    solution = Solution()
    test1 = [1,2,3,1]
    test2 = [1,0,1,1]
    test3 = [1,2,3,1,2,3]
    print(solution.containsNearbyDuplicate(test1, 3))
    print(solution.containsNearbyDuplicate(test2, 1))
    print(solution.containsNearbyDuplicate(test3, 2))
