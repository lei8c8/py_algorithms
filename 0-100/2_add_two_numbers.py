
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        l1_list = self.traversalList(l1)
        l2_list = self.traversalList(l2)
        l1_list = [str(i) for i in l1_list]
        l2_list = [str(i) for i in l2_list]
        sum_val = int(''.join(l1_list)) + int(''.join(l2_list))
        sum_val_reverse = [int(i) for i in str(sum_val)[::-1]]
        res = self.createList(sum_val_reverse)
        return res

    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
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

if __name__ == "__main__":
    solution = Solution()
    list1_node1 = ListNode(2)
    list1_node2 = ListNode(4)
    list1_node3 = ListNode(3)
    list1_node1.next = list1_node2
    list1_node2.next = list1_node3
    list1_head = list1_node1

    list2_node1 = ListNode(5)
    list2_node2 = ListNode(6)
    list2_node3 = ListNode(4)
    list2_node1.next = list2_node2
    list2_node2.next = list2_node3
    list2_head = list2_node1
