from treeNode import Node
from collections import deque

class BST:
    def __init__(self):
        self.root = None
        self.result = []

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current # remember parent node
                if node.data <= current.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = node 
                        return

    def getParentAndNode(self, data):
        parent = None
        current = self.root
        if current is None:
            return (parent, None)
        else:
            while True:
                if current.data == data:
                    return (parent, current)
                elif current.data > data:
                    parent = current
                    current = current.left
                else:
                    parent = current
                    current = current.right
        return (parent, current)
    
    def remove(self, data):
        parent, node = self.getParentAndNode(data)
        if parent is None and node is None:
            return False
        # variable for count of children
        countOfChildren = 0
        if (node.left is None) and (node.right is None):
            pass
        elif node.left and node.right:
            countOfChildren = 2
        else:
            countOfChildren = 1
        # simple deletion if no children
        if countOfChildren == 0:
            if not parent:
                self.root = None
            else:
                if parent.left is node:
                    parent.left = None
                else: 
                    parent.right = None
        # one child case, parent point to node's child
        elif countOfChildren == 1:
            nextNode = None
            if node.left:
                nextNode = node.left
            else:
                nextNode = node.right
            if parent:
                if parent.left is node:
                    parent.left = nextNode
                else:
                    parent.right = nextNode
            # special case when the node is root
            else:
                self.root = nextNode
        # the most complicated case, two children
        else:
            parentOfLeftMostNode = node
            leftMostNode = node.right
            while leftMostNode.left:
                parentOfLeftMostNode = leftMostNode
                leftMostNode = leftMostNode.left
            # change the node's data with left most node
            node.data = leftMostNode.data
            if parentOfLeftMostNode.left == leftMostNode:
                parentOfLeftMostNode.left = leftMostNode.right
            else:
                parentOfLeftMostNode.right = leftMostNode.right

    def inorder(self, root):
        '''in order depth first traversal'''
        current = root
        if current is None:
            return
        self.inorder(current.left)
        #print(current.data)
        self.result.append(current.data)
        self.inorder(current.right)

    def preorder(self, root):
        '''preorder depth first traversal'''
        current = root
        if current is None:
            return
        self.result.append(current.data)
        self.preorder(current.left)
        self.preorder(current.right)
    
    def postorder(self, root):
        '''post order depth first traversal'''
        current = root
        if current is None:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        self.result.append(current.data)

    def breadthFirstTraversal(self):
        result = []
        traversalQueue = deque([self.root])
        while len(traversalQueue) > 0:
            current_node = traversalQueue.popleft()
            result.append(current_node.data)
            if current_node.left:
                traversalQueue.append(current_node.left)
            if current_node.right:
                traversalQueue.append(current_node.right)
        return result
    
    def size(self):
        return len(self.breadthFirstTraversal())

    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return None
            elif current.data == data:
                return data
            elif current.data > data:
                current = current.left
            else:
                current = current.right

if __name__ == '__main__':
    tree = BST()
    # test insert method, inorder traversal
    tree.insert(5)
    tree.insert(7)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(6)
    tree.inorder(tree.root)
    print("Inorder Traversal Result:")
    print(tree.result)

    tree = BST()
    # test insert method, preorder traversal
    tree.insert(5)
    tree.insert(7)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(6)
    tree.preorder(tree.root)
    print("Preorder Traversal Result:")
    print(tree.result)

    tree = BST()
    # test insert method, postorder traversal
    tree.insert(5)
    tree.insert(7)
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(6)
    tree.postorder(tree.root)
    print("Postorder Traversal Result:")
    print(tree.result)
    print(f"Size: {tree.size()}")
