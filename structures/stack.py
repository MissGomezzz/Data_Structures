# This is an implementation of the stack data structure, which is based on the LIFO principle
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            print ("The stack is empty. There aren't elements to pop")
            return
        element = self.head
        self.head = self.head.next
        print (f"The stack just popped element {element.data}. ")
        return element.data

    def peek(self):
        if self.head is None:
            print ("The stack is empty. Nothing to peek here")
            return
        element = self.head
        print (f"We peeked and saw the element {element.data}. ")
        return element.data

    def print_stack(self):
        if self.head is None:
            print ("Nothing to print here, the stack is empty. ")
            return
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

stack = Stack()
stack.pop()
stack.peek()
stack.push(1)
stack.pop()
stack.pop()