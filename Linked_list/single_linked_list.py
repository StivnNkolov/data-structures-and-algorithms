"""
Linked list is a form of sequential collection, and it does not have to be in order. A linked list is made up from
independent nodes that may contain any type of data and each node has a reference to the next node in the link.
To reach the last node we must traverse all the nodes before the last one. The linked list in memory is not contiguous.
LL always has head and tail. Nodes contain two parts: first is the data and the second is the reference to the next node (link).
The size of LL is not predefined. Removal and insertion in LL are very efficient in comparison to Array. To find element in LL we
always need to traverse the LL(in comparison with List;Array).
There are 4 types of LL: Singly linked list; Circular linked list; Doubly linked list; Circular doubly linked list.
The location of nodes in memory are always randomly placed.
"""


# Creating Singly Linked List
# TC for creating SLL = O(1); SC for creating one node = O(1) SC for creating more nodes = O(n)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # To print the SLL
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert in SSL
    def insert_in_ssl(self, value, location=0):  # TC O(n) SC O(1)
        # First we create the new node we want to add to the SLL
        new_node = Node(value)
        # Check to see if we have any nodes in our SLL. (If the SLL is empty)
        if self.head is None:
            # We add the first node to our empty SLL
            self.head = new_node
            self.tail = new_node
        else:
            # If the location is 0 this means we want to add new node to the beginning of the SLL.
            if location == 0:  # TC O(1)
                """
                We know that the head contains reference to the first node, that is why we add the head as new_node.next 
                """
                new_node.next = self.head
                self.head = new_node
            # If the location is -1 we want to add element to the end of the SLL
            elif location == -1:  # TC O(1)
                # We know that the last element link is None
                new_node.next = None
                # This is how we reach the current last element and add to its link reference to the new node.
                self.tail.next = new_node
                # Then we add to the tail reference to the new element
                self.tail = new_node
                # This cycle is breaking the connection between the tail and the old last element, and add the new element at the beginning.
            # In every other case we want to add element to location in the middle of the SLL
            else:  # TC O(n)
                # First we need to loop over the elements to find the current element that stands in the position we want.
                # By doing this loop we find the node that stands at the location where we want to add the new node.
                # # Line 65 66 are added by me to fix bug with SLL with one element but location is set to 2 or more
                # if self.head == self.tail:
                #     location = 1
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                """
                Current node is the node at the position that we want to add the new node.
                By doing the next 3 lines of code we are inserting the new node between the current node and the next node.
                """
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                if current_node == self.tail:
                    self.tail = new_node

    #  Traverse SLL
    def traverse_sll(self):  # TC O(n) SC O(1)
        # Check if the SLL exist.
        if self.head is None:
            print('The SLL is empty.')
        else:
            # By using the head we find the first node to start from.
            current_node = self.head
            # We loop until we find the last element which next value will be None.
            while current_node is not None:
                print(current_node.value)
                # We set current node to current_node.next to actually go to the next value in the SSL.
                current_node = current_node.next

    # Search in SLL
    def search_in_sll(self, searched_value):  # TC O(n) SC O(1)
        # Check if the SLL is empty
        if self.head is None:
            return 'The list does not exist'
        # Else:
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == searched_value:
                return f'{searched_value} is at position {index}'
            current_node = current_node.next
            index += 1
        return f'{searched_value} does not exist in the list'

    # Deleting node from SLL
    def delete_node(self, location):  # TC O(n) SC O(1)
        # First we check if the SLL exist
        if self.head is None:
            print('The SLL does not exist')
        else:
            # If location is 0 that means we want to delete the first node
            # In this case we have two cases. SLL with only one node and SLL with more than one node
            if location == 0:
                # this condition will be true if we have only one node
                if self.head == self.tail:
                    # This way we delete the only node in the SLL
                    self.head = None
                    self.tail = None
                # This condition will be true if we have more than one node.
                else:
                    """
                    We access the second node with self.head.next. Then we set the head to the second node we accessed
                    and the garbage collector will automatically delete the first node.
                    """
                    self.head = self.head.next
            # Second case is location to be -1 witch means we want to delete the last node.
            elif location == -1:
                # this condition will be true if we have only one node
                if self.head == self.tail:
                    # This way we delete the only node in the SLL
                    self.head = None
                    self.tail = None
                # This condition will be true if we have more than one node.
                else:
                    # We need to traverse the SLL until we reach to the second to last node.
                    current_node = self.head
                    while current_node is not None:
                        if current_node.next == self.tail:
                            break
                        current_node = current_node.next
                    current_node.next = None
                    self.tail = current_node
            # In this condition we have location somewhere in the middle of the SLL
            else:
                # After the loop current_node will be the node before the one we want to delete
                node_before_the_one_we_want_to_delete = self.head
                index = 0
                while index < location - 1:
                    node_before_the_one_we_want_to_delete = node_before_the_one_we_want_to_delete.next
                    index += 1
                # Next node is actually the node we want to delete
                node_we_want_to_delete = node_before_the_one_we_want_to_delete.next
                """
                 to break the connection between the node before the one we want to delete and the node after the one 
                we want to delete we set the current_node.next to next_node.next.
                """
                # To access the node after the one we want to delete we use the node that we want to delete next reference.
                node_before_the_one_we_want_to_delete.next = node_we_want_to_delete.next

    # Delete entire SLL
    def delete_sll(self):  # TC O(1) SC O(1)
        if self.head is None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None


singly_linked_list = SinglyLinkedList()
# print(singly_linked_list.search_in_sll(55))

singly_linked_list.insert_in_ssl(1, 0)
singly_linked_list.insert_in_ssl(2, 1)
singly_linked_list.insert_in_ssl(20, 1)

singly_linked_list.insert_in_ssl(3, 2)
singly_linked_list.insert_in_ssl(4, 3)

print([node.value for node in singly_linked_list])
singly_linked_list.delete_node(1)

print([node.value for node in singly_linked_list])

# singly_linked_list.traverse_sll()
# Creating new SLL
# node_1 = Node(1)
# node_2 = Node(2)
# node_3 = Node(3)
#
# singly_linked_list.head = node_1
# singly_linked_list.head.next = node_2
# singly_linked_list.tail = node_2
