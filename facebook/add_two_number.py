# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        twoSum = str(int(self.getNumber(l1)) + int(self.getNumber(l2)))
        return self.constructList(twoSum)
    
    def getNumber(self, head):
        current, res = head, []
        while current:
            res.append(str(current.val))
            current = current.next
        return ''.join(res[::-1])

    def constructList(self, num):
        head = ListNode(int(num[-1]))
        current = head
        for i in range(len(num) - 2, -1, -1):
            node = ListNode(int(num[i]))
            current.next = node
            current = current.next
        return head

