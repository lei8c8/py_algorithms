class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        lookup, mappingList = {}, []
        for i, v in enumerate(B):
            lookup[v] = i
        for i in range(len(A)):
            mappingList.append(lookup[A[i]])
        return mappingList

if __name__ == "__main__":
    solution = Solution()
    testdata1 = [12, 28, 46, 32, 50]
    testdata2 = [50, 12, 32, 46, 28]
    result = solution.anagramMappings(testdata1, testdata2)
    print(result)
        