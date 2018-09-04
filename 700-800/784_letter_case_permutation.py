class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        stack = list(S)
        res = ['']
        while stack:
            ch = stack.pop()
            if ch.isalpha():
                res = [ch.lower() + x for x in res] + [ch.upper() + x for x in res]
            else:
                res = [ch + x for x in res]
        return res
