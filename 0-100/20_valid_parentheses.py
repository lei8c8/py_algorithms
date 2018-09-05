class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for element in s:
            if element in '({[':
                stack.append(element)
            else:
                try:
                    if element == ')':
                        if stack.pop() == '(':
                            continue
                        else:
                            return False
                    if element == '}':
                        if stack.pop() == '{':
                            continue
                        else:
                            return False                            
                    if element == ']':
                        if stack.pop() == '[':
                            continue
                        else:
                            return False
                except:
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()
    testdata = "([)]"
    result = solution.isValid(testdata)
    print(result)