# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        steps, res = [], []
        node_number = self.getNodeNumber(root)
        if node_number == 0:
            return [[]] * k
        step_n, step_m = node_number // k, node_number % k
        steps = [step_n] * k
        for i in range(step_m):
            steps[i] += 1
        current, prev = root, root
        res.append(current)
        for i in steps[:-1]:
            for _ in range(i):
                prev = current
                current = current.next
            res.append(current)
            prev.next = None
        return res

    def getNodeNumber(self, root):
        cur, res = root, 0
        if not cur: return 0
        while cur:
            res += 1
            cur = cur.next
        return res