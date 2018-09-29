class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.lookup:
            self.lookup[number] = 1
        else:
            self.lookup[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            if value - key in self.lookup:
                if value - key == key and self.lookup[key] > 1:
                    return True
                elif value - key == key and self.lookup[key] == 1:
                    continue
                else:
                    return True
        return False
