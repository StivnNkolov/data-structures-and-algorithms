"""
In the CDLL the first node's prev reference points to the last node and the last node's next reference points
to the first node. This is the difference between DLL and CDLL.
This way we can not only traverse forward and backward but we can loop from start to end and from end to start easily.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            # If the curr node is the same as the first node we break the loop.
            if node == self.tail.next:
                break

    def __cddl_exist(self):
        if self.head is None:
            raise FileNotFoundError('The CDLL does not exist')

    def create_cdll(self, node_value):  # TC O(1) SC O(1)
        node = Node(node_value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
        return f'Successfully created CDLL with node {node_value}'

    def insert(self, node_value, location):  # TC O(n) SC O(1)
        self.__cddl_exist()

        new_node = Node(node_value)

        if location == 0:
            # connection between new node's next ref and the old first node.
            new_node.next = self.head
            # connection between new node's prev ref to the last node.
            new_node.prev = self.tail
            # reverse connection between the old first node and the new first node.
            self.head.prev = new_node
            # connection between head and new node.
            self.head = new_node
            # connection between the last node's next reference and the new node.
            self.tail.next = new_node
            return f'Successfully inserted node {node_value} at first position.'

        if location == -1:
            # connection between the new last node and the first node.
            new_node.next = self.head
            # reverse connection between the new last node and the old last node.
            new_node.prev = self.tail
            # reverse connection between first node and new last node.
            self.head.prev = new_node
            # connection between old last node and new node.
            self.tail.next = new_node
            # connection between tail and new node.
            self.tail = new_node
            return f'Successfully inserted node {node_value} at last position.'

        previous_node = self.head
        index = 0

        while index < location - 1:
            previous_node = previous_node.next
            index += 1
        # link between new node and the node after the previous node.
        new_node.next = previous_node.next
        # reverse link between new node and previous node.
        new_node.prev = previous_node
        # reverse link between the next node and the new node.
        previous_node.next.prev = new_node
        # link between previous node and new node.
        previous_node.next = new_node
        return f'Successfully inserted node {node_value} at position {location}'

    def traverse(self):  # TC O(n) SC O(1)
        self.__cddl_exist()
        current_node = self.head

        while True:
            print(current_node.value)
            if current_node == self.tail:
                break
            current_node = current_node.next

    def reverse_traverse(self):  # TC O(n) SC O(1)
        self.__cddl_exist()

        current_node = self.tail
        while True:
            print(current_node.value)
            if current_node == self.head:
                break
            current_node = current_node.prev

    def search_value(self, node_value):  # TC O(n) SC O(1)
        self.__cddl_exist()

        current_node = self.head
        index = 0
        while True:
            if current_node.value == node_value:
                return f'Node with value {node_value} was found on position {index}'
            if current_node == self.tail:
                return f'Node with value {node_value} was not found.'
            current_node = current_node.next
            index += 1

    def delete_node(self, location):  # TC O(n) SC O(1)
        self.__cddl_exist()
        # If we want to delete the first node.
        if location == 0:
            if self.head == self.tail:
                # Deleting all references to the only node.
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
                return 'Successfully deleted the only node in the CDLL.'
            # Link between head and the second node.
            self.head = self.head.next
            # reverse link between the new first node and the last node.
            self.head.prev = self.tail
            # link between the last node and the new first node.
            self.tail.next = self.head
            return f'Successfully deleted first node.'
        if location == -1:
            if self.head == self.tail:
                # Deleting all references to the only node.
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
                return 'Successfully deleted the only node in the CDLL.'
            # link between tail and second to last node.
            self.tail = self.tail.prev
            # link between the new last element and the first element.
            self.tail.next = self.head
            # reverse link between first element and the new last element.
            self.head.prev = self.tail
            return f'Successfully deleted last node.'

        previous_node = self.head
        index = 0
        # Loop until the node before the one we want to delete.
        while index < location - 1:
            previous_node = previous_node.next
            index += 1
        # link between the node before the one we want to delete and the node after the one we want to delete.
        previous_node.next = previous_node.next.next
        # reverse link between the node after the one we want to delete and the one before the one we want to delete.
        previous_node.next.prev = previous_node
        return f'Successfully deleted node at position {location}'

    def delete_cdll(self):  # TC O(n) SC O(1)
        """
        In SLL if we set head and tail to none the whole SLL is deleted. In CDLL, because every node keeps reference to
        the previous node this is not the case.
        If we want to delete the whole CDLL we need to set all node's prev reference to None and the last node next
        reference to None.
        """
        self.__cddl_exist()
        self.tail.next = None
        current_node = self.head

        while current_node:
            current_node.prev = None
            current_node = current_node.next
        self.head = None
        self.tail = None
        return 'The CDLL has been successfully deleted.'


test = CDLL()
print(test.create_cdll(5))
print(test.insert(0, 0))
print(test.insert(1, -1))
print(test.insert(2, 2))
print([node.value for node in test])
# test.traverse()
# print('----')
# test.reverse_traverse()
# print(test.search_value(33))
# print(test.delete_node(-1))
print(test.delete_cdll())
print([node.value for node in test])
