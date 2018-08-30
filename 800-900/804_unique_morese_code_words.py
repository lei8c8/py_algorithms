class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = set()
        for word in words:
            temp = []
            for c in word:
                temp.append(self.helper(c))
                tempStr = ''.join(temp)
            res.add(tempStr)
        return len(res)

    def helper(self, c):
        myList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return myList[ord(c) - ord('a')]

if __name__ == "__main__":
    solution = Solution()
    result = solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(result)