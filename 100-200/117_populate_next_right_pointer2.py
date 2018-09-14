from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        queue = deque([root])
        while queue:
            level_len = len(queue)
            while level_len > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_len -= 1
                if level_len == 0:
                    node.next = None
                else:
                    next_node = queue[0]
                    node.next = next_node