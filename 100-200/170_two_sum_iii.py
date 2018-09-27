class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.items.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        lookup = {}
        for i, v in enumerate(self.items):
            if v not in lookup:
                lookup[v] = 1
            else:
                lookup[v] += 1
        for element in lookup:
            if (value - element) in lookup and (value - element) != element:
                return True
            if (value - element) in lookup and (value - element) == element and lookup[element] > 1:
                return True
        return False