"""
Circular singly linked list = same as singly linked list. The only difference is that, the last node in CSLL points to
the first node (in SLL the last node's next reference is null).
When we have only one node, this node points to itself.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def create_csll(self, node_value):  # TC O(1) SC O(1)
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node

        return 'The CSLL has been created.'

    def insert(self, value, location):  # TC O(n) SC O(1)
        # First we check if the CSLL exists.
        if self.head is None:
            return 'The CSLL does not exist.'

        new_node = Node(value)

        # We start checking for the location that we want to insert at.
        if location == 0:
            # We set the old first node to be the new node's next reference.
            new_node.next = self.head
            # We make connection between the head and the new node.
            self.head = new_node
            """
            In CSLL the last element must point to the first element.
            self.tail is reference to the last node. We make connection between the last node and the first node,
            using the self.tail.next.
            """
            self.tail.next = new_node
            return f'The value {value} was inserted at the beginning of the CSLL.'
        if location == -1:
            # self.tail.next is the first node. This way we make the connection between the new last node and the first.
            new_node.next = self.tail.next
            # We make connection between the new_node and the old last node.
            self.tail.next = new_node
            # We make the connection between the tail and the new node.
            self.tail = new_node
            return f'The value {value} was inserted at the end of the CSLL.'

        # Here we cover the case when the location is somewhere in the middle of the CSLL.
        current_node = self.head
        index = 0
        # We loop until we reach the node before the position that we want.
        while index < location - 1:
            current_node = current_node.next
            index += 1
        # This way we obtain the node that will be after the node we want to insert.
        next_node = current_node.next
        # We make the connection between the node before the new_one and the new_one.
        current_node.next = new_node
        # We set the new_node's next reference to point to the next_node.
        new_node.next = next_node
        return f'The value {value} was inserted at index {location}.'

    def traverse(self):  # TC O(n) SC O(1)
        if self.head is None:
            return 'The CSLL does not exist.'

        current_node = self.head
        while True:
            print(current_node.value)
            if current_node.next == self.head:
                break
            current_node = current_node.next

    def search_value(self, node_value):  # TC O(n) SC O(1)
        if self.head is None:
            return 'The CSLL does not exist.'

        current_node = self.head
        index = 0

        while True:
            if current_node.value == node_value:
                return f'The value {node_value} was found on index {index}'
            if current_node.next == self.head:
                break
            current_node = current_node.next
            index += 1

        return f'The value {node_value} does not exist in the CSLL.'

    def delete_node(self, location):  # TC O(n) SC O(1)
        if self.head is None:
            return 'The csll is empty.'
        if self.head == self.tail:
            self.head.next = None
            self.head = None
            self.tail = None
            return 'You deleted the only node in the csll.'

        if location == 0:
            # We connect the second element with the head. self.head.next=the second element.
            self.head = self.head.next
            # We connect the last element with the first element.
            self.tail.next = self.head
            return 'You deleted element at index 0.'
        if location == -1:
            node_before_the_one_we_want_to_delete = self.head

            while True:
                # If the next node is == tail, this means we are in the node before the last node.
                if node_before_the_one_we_want_to_delete.next == self.tail:
                    break
                node_before_the_one_we_want_to_delete = node_before_the_one_we_want_to_delete.next
            # Connection between the node and the first element.
            node_before_the_one_we_want_to_delete.next = self.head
            # Connection between the node and the tail.
            self.tail = node_before_the_one_we_want_to_delete
            return 'You deleted the last node.'

        node_before_the_one_we_want_to_delete = self.head
        index = 0
        # index < location - 1 will get us to the node before the on we want to delete
        while index < location - 1:
            node_before_the_one_we_want_to_delete = node_before_the_one_we_want_to_delete.next
            index += 1
        node_we_want_to_delete = node_before_the_one_we_want_to_delete.next
        node_before_the_one_we_want_to_delete.next = node_we_want_to_delete.next
        return f'You deleted node at location {location}'

    def delete_csll(self):  # TC O(n) SC O(1)
        if self.head is None:
            return 'The CSLL does not exist.'
        self.head = None
        self.tail.next = None
        self.tail = None
        return 'You deleted the CSLL'


csll = CSLL()
print(csll.create_csll(1))
print(csll.insert(3, -1))
print(csll.insert(4, -1))
print(csll.insert(5, -1))
print(csll.insert(6, 0))
print(csll.insert(7, 1))
print(csll.insert(8, 7))

# csll.traverse()
# print(csll.search_value(8))
# print(csll.insert(2, -1))

# print(csll.delete_node(1))
print([el.value for el in csll])
print(csll.delete_csll())
print([el.value for el in csll])
