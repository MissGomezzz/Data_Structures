# This is an implementation of the Binary Tree, which uses nodes and hierarchy to store data in an organized way
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return None
        self._insert_recursive(self.root,data)
        return None

    #Helper recursive function used to rather create a node (child) or return the existing one
    def _insert_recursive(self,node,data):
        if node is None:
            return Node(data)
        if data <= node.data:
            node.left = self._insert_recursive(node.left,data)
        if data > node.data:
            node.right = self._insert_recursive(node.right,data)
        return node

    def search(self,data):
        if self.root is None:
            print ("Nothing to search here: binary tree empty. ")
            return None
        result = self._search_recursive(self.root,data)
        if result:
            print (f"Element {data} found. ")
        else:
            print (f"Element {data} not found. ")
        return None

    # Helper recursive function used to scan the binary tree for a specific set of data
    def _search_recursive(self,node,data):
        if node is None:
            return False
        if data == node.data:
           return True
        if data < node.data:
            return self._search_recursive(node.left, data)
        if data > node.data:
            return self._search_recursive(node.right, data)
        return None

    def delete(self,data):
        if self.root is None:
            print ("Nothing to delete here: binary tree empty. ")
            return None
        self._delete_recursive(self.root,data)

    def _delete_recursive(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Found the node to delete
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # case 3 - two children
        return node


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)

tree.search(3)   # should find it
tree.search(8)   # should find it
tree.search(99)  # should not find it
