class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = self.traversalList(l1)
        l2_list = self.traversalList(l2)
        l1_list = [str(i) for i in l1_list]
        l2_list = [str(i) for i in l2_list]
        sum_val = int(''.join(l1_list)) + int(''.join(l2_list))
        sum_val = [int(i) for i in str(sum_val)]
        res = self.createList(sum_val)
        return res

    def traversalList(self, head):
        res = []
        if not head:
            return None
        current = head
        while current:
            res.append(current.val)
            current = current.next
        return res  

    def createList(self, n):
        pre = ListNode(0)
        before_head = pre
        for i in n:
            node = ListNode(i)
            pre.next = node
            pre = node
        return before_head.next