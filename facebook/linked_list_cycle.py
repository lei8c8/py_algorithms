class Solution(object):
    def hasCycle(self, head):
        try:
            slow, fast = head, head.next
            while slow is not fast:
                slow, fast = slow.next, fast.next.next
            return True
        except:
            return False