"""
In the SLL, every node contains reference to the next node. The reverse
traversal is not possible. In the DLL each node contains two references,
to the previous and the next node. In both ways the traversal is possible.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __ddl_exist(self):
        if self.head is None:
            raise FileNotFoundError('The DLL does not exist')

    def create_dll(self, node_value):  # TC O(1) SC O(1)
        node = Node(node_value)
        self.head = node
        self.tail = node
        return 'Successfully created DLL.'

    def insert(self, value, location):  # TC O(n) SC O(1)
        self.__ddl_exist()

        new_node = Node(value)

        # Insert in beginning of dll.
        if location == 0:
            # making the new node to None (it is by default like this????)
            new_node.prev = None
            # making the new node's next reference to the old first node.
            new_node.next = self.head
            # making connection between the old first node and the new node.
            self.head.prev = new_node
            # making connection between head and new node.
            self.head = new_node
            return f'Successfully inserted node with value {value} at position 0.'
        # Insert at the end.
        if location == -1:
            new_node.next = None
            # reverse connection between new node and the old last node.
            new_node.prev = self.tail
            # making connection between old last node and the new node.
            self.tail.next = new_node
            # connection between tail and new node.
            self.tail = new_node
            return f'Successfully inserted node with value {value} at last position.'
        # Insert somewhere in the middle of the dll.
        node_at_position_before_the_one_we_need_to_insert = self.head
        index = 0
        # Loop until we got to the location - 1
        while index < location - 1:
            node_at_position_before_the_one_we_need_to_insert = node_at_position_before_the_one_we_need_to_insert.next
            index += 1
        # making connection between the new node and the node that will be next in the dll.
        new_node.next = node_at_position_before_the_one_we_need_to_insert.next
        # reverse connection between new node and the node we want to be before the new node.
        new_node.prev = node_at_position_before_the_one_we_need_to_insert
        """
        node_at_position_before_the_one_we_need_to_insert.next=reference to the node we want to be after new node.
        node_at_position_before_the_one_we_need_to_insert.next.prev=reverse connection between the above and the new one
        line 79=connection between node before the one we want to insert and the new node.
        node_at_position_before_the_one_we_need_to_insert=node at location - 1.
        node_at_position_before_the_one_we_need_to_insert.next=node we want to be after the new node.
        node_at_position_before_the_one_we_need_to_insert.next.prev=previous reference for the
        node we want to be after the new node and the new node.
        """
        node_at_position_before_the_one_we_need_to_insert.next.prev = new_node
        node_at_position_before_the_one_we_need_to_insert.next = new_node
        return f'Successfully inserted node with value {value} at position {location}'

    def traverse(self):  # TC O(n) SC O(1)
        self.__ddl_exist()
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse_travers(self):  # TC O(n) SC O(1)
        self.__ddl_exist()
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search_value(self, node_value):  # TC O(n) SC O(1)
        self.__ddl_exist()
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == node_value:
                return f'Node with value {node_value} was found on position {index}'
            current_node = current_node.next
            index += 1
        return f'Node with value {node_value} was not found.'

    # We delete node from first place, last place or any location in the middle without first and last!!
    def delete_node(self, location):  # TC O(n) SC O(1)
        self.__ddl_exist()

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return 'Successfully deleted the only node'
            # self.head.next = second node in the dll. Connection between head and second node.
            self.head = self.head.next
            # making the new first node prev reference to None
            self.head.prev = None
            return f'Successfully deleted first node.'
        if location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return 'Successfully deleted the only node'
            # self.tail.prev=node second to last. Making connection between tail and second to last node.
            self.tail = self.tail.prev
            # making the new last node next reference to none
            self.tail.next = None
            return f'Successfully deleted last node.'

        # This will work only if the location is not first or last. Only for middle nodes.

        node_before_the_one_we_want_to_delete = self.head
        index = 0
        # Loop until we reach the node before the one we want to delete.
        while index < location - 1:
            node_before_the_one_we_want_to_delete = node_before_the_one_we_want_to_delete.next
            index += 1
        """
        node_before_the_one_we_want_to_delete.next.next=node after the one we want to delete.
        line 153=making connection between the node before the one that we want to delete, and the node after the one 
        we want to delete.
        line 154=making reverse connection between the node before the one we want to delete and the node after the one 
        we want to delete.
        With those two steps we break the connection between the node before the one we want to delete and the node we
        want to delete and the node after the one we want to delete and the node we want to delete.
        We just connect the node before and after the one that we want to delete.
        """
        node_before_the_one_we_want_to_delete.next = node_before_the_one_we_want_to_delete.next.next
        node_before_the_one_we_want_to_delete.next.prev = node_before_the_one_we_want_to_delete
        return f'Successfully deleted node at position {location}'

    def delete_dll(self):  # TC O(n) SC O(1)
        """
        Because the nodes in dll are connected in both ways between them, they will not be deleted by the garbage coll.,
        if we simply make the head and tail no null. That is why we need to loop and change every node's prev reference
        to None.
        """
        self.__ddl_exist()
        current_node = self.head
        while current_node:
            current_node.prev = None
            current_node = current_node.next
        self.head = None
        self.tail = None
        return 'The dll has been successfully deleted.'


test = DLL()
print(test.create_dll(5))
print(test.insert(0, 0))
print(test.insert(2, -1))
print(test.insert(6, 2))
print([node.value for node in test])
# test.traverse()
# print('------')
# test.reverse_travers()
# print(test.search_value(99))
print(test.delete_node(1))
# print(test.delete_node(-1))
# print(test.delete_node(0))
print([node.value for node in test])
