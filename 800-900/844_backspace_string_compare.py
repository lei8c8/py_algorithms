class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.push_valid_in_stack(S) == self.push_valid_in_stack(T)

    def push_valid_in_stack(self, string):
        i = len(string) - 1
        stack = []
        backspace = 0
        while i >= 0:
            if string[i] == "#":
                backspace += 1
            elif string[i] != "#":
                if backspace == 0:
                    stack.append(string[i])
                else:
                    backspace -= 1
            i -= 1
        return stack

if __name__ == "__main__":
    solution = Solution()
    S = "ab##"
    T = "c#d#"
    print(solution.backspaceCompare(S, T))