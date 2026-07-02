# This is an implementation of the queue data structure, which is based on the FIFO principle

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        node.next = self.tail
        self.tail = node

