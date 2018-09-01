class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]:
            return letters[0]
        low = 0
        high = len(letters) - 1
        while low <= high:
            middle = (low + high) // 2
            if letters[middle] > target:
                high = middle - 1
            elif letters[middle] <= target:
                low = middle + 1
                while letters[low] == target:
                    low += 1
        return letters[low]
        

if __name__ == "__main__":
    solution = Solution()
    testdata = ["c", "f", "j"]
    result = solution.nextGreatestLetter(testdata, "a")
    print(result)