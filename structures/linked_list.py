# This is an implementation of the linked list, which is based on the use of nodes in order to store data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def print_list(self):
        if self.head is None:
            print ("The list is empty")
            return
        current = self.head
        while current.next is not None:
            print (current.data)
            current = current.next
        print (current.data)

    def search(self, data):
        position = 1
        if self.head is None:
            print ("The list is empty. Data not found")
            return
        current = self.head
        while current.next is not None:
            if data == current.data:
                print(f"Element {data} found at position {position}")
                return
            current = current.next
            position+= 1

        if data == current.data:
            print (f"Element {data}  found at position {position} ")
            return
        print (f"Element {data} not found. ")

    def length(self):
        size = 0
        if self.head is None:
            print (f"The list is empty, with a length of {size}")
        current = self.head
        while current.next is not None:
            size+= 1
            current = current.next
        print (f"The current length of the linkedlist is {size+1}")


    def delete(self,data):
        if self.head is None:
            print ("The list is empty. Data not found")
            return
        current = self.head

        if self.head.data == data:
            self.head = self.head.next
            print(f"Element {data} deleted. ")
            return

        while current.next is not None:
            if data == current.next.data:
                current.next = current.next.next
                print(f"Element {data} deleted. ")
                return
            current = current.next

        if data == current.data:
            prev = current
            prev.next = current.next
            print (f"Element {data} deleted. ")
            return
        print (f"Element {data} not found. ")



lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

lista.print_list()

lista.search(2)
lista.length()
lista.delete(5)

lista.print_list()
