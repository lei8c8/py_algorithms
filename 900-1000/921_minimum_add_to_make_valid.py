class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for element in S:
            if stack and element == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(element)
        return len(stack)