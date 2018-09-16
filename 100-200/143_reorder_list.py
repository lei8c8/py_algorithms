# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        current = head
        queue = deque([])
        while current:
            queue.append(current)
            current = current.next      
        prev = ListNode(0)
        while len(queue) > 1:
            n1 = queue.popleft()
            prev.next = n1
            n2 = queue.pop()
            prev = n2
            n1.next = n2
        prev.next = None
        try:
            n = queue.pop()
            prev.next = n
            n.next = None
        except:
            pass
        

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    #n4.next = n5
    solution = Solution()
    solution.reorderList(n1)
    current = n1
    while current:
        print(current.val, end= "->")
        current = current.next


