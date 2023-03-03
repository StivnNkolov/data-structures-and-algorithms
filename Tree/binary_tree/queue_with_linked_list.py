"""
Implementation of queue with Linked List.
Head points to the first added element in the queue.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):  # TC O(1) SC O(1)
        self.items = LinkedList()

    def __str__(self):
        values = [str(el) for el in self.items]
        return ' '.join(values)

    def is_empty(self):
        if self.items.head is None:
            return True
        return False

    # When we add element to the queue we always set it to the en of the LL
    def enqueue(self, value):  # TC O(1) SC O(1)
        node = Node(value)

        # Checking if the LL is empty.
        if self.items.head is None:
            self.items.head = node
            self.items.tail = node
        else:
            self.items.tail.next = node
            self.items.tail = node
        return f'Successfully added element {value} in the queue.'

    def dequeue(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The queue is empty'

        current_element = self.items.head
        # Checking if this is the only el in the queue
        if self.items.head == self.items.tail:
            self.items.head = None
            self.items.tail = None
        else:
            # Creating link between head and second node.
            self.items.head = self.items.head.next
        return current_element

    def peek(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The queue is empty'
        return self.items.head

    def delete_queue(self):  # TC O(1) SC O(1)
        self.items.head = None
        self.items.tail = None
        return 'The queue was successfully deleted.'

