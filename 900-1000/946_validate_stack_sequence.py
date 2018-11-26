class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        popped_time = 0
        stack = []
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[popped_time] and popped_time < len(pushed):
                stack.pop()
                popped_time += 1
        return popped_time == len(pushed)