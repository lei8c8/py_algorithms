class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        b = []
        while tokens:
            a = tokens.pop(0)
            if a == '+':
                b.append(b.pop(-2) + b.pop(-1))
            elif a == '-':
                b.append(b.pop(-2) - b.pop(-1))
            elif a == '*':
                b.append(b.pop(-2) * b.pop(-1))
            elif a == '/':
                b.append(int(b.pop(-2) / b.pop(-1)))
            else:
                b.append(int(a))
        return b[0]