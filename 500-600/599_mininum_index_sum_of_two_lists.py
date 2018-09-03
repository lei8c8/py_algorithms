class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        dict1 = {}
        dict2 = {}
        sum = len(list1) + len(list2) - 2
        for k, v in enumerate(list1):
            dict1[v] = k
        for k, v in enumerate(list2):
            dict2[v] = k
        for i in range(len(list2)):
            if list2[i] in dict1:
                temp_sum = i + dict1[list2[i]]
                if temp_sum < sum:
                    sum = temp_sum
        #print(set(list1).intersection(set(list2)))
        for element in set(list1).intersection(set(list2)):
            if dict1[element] + dict2[element] == sum:
                res.append(element)
        return res

if __name__ == "__main__":
    solution = Solution()
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    result = solution.findRestaurant(list1, list2)
    print(result)