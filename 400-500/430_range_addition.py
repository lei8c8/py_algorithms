class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        myList = [0] * length
        for update in updates:
            for i in range(update[0], update[1] + 1):
                myList[i] += update[2]
        return myList