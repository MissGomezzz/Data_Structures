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
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            print ("The queue is empty. There isn't an item available to dequeue")
            return None
        element = self.head
        self.head = self.head.next
        print (f"Element {element.data} dequeued.")
        if self.head is None:
            self.tail = None
        return element.data

    def peek(self):
        if self.head is None:
            print ("Nothing to peek here: Queue empty")
            return None
        element = self.head
        print (f"Element {element.data} peeked.")
        return element.data

    def print_queue(self):
        if self.head is None:
            print ("The queue is empty.")
            return None
        element = self.head
        while element is not None:
            print (f"Element {element.data}")
            element = element.next
        return None

queue = Queue()
queue.dequeue()        # empty queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()
queue.dequeue()
queue.print_queue()
queue.dequeue()
queue.dequeue()
queue.dequeue()        # empty again