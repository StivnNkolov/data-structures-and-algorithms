"""
The last element inserted in the stack will be the first element in the LL.
The head will always point to the last element in.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    # Creating empty stack
    def __init__(self):  # TC O(1) SC O(1)
        self.linked_list = LinkedList()

    def is_empty(self):  # TC O(1) SC O(1)
        if self.linked_list.head is None:
            return True
        return False

    def __str__(self):
        values = [str(el.value) for el in self.linked_list]
        return '\n'.join(values)

    def push(self, value):  # TC O(1) SC O(1)
        # Create node
        new_node = Node(value)
        # Link between new node and the old first node.
        new_node.next = self.linked_list.head
        # Link between head and new first node.
        self.linked_list.head = new_node
        return f'The element {value} has been successfully inserted.'

    def pop(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The stack is empty.'
        current_node = self.linked_list.head

        self.linked_list.head = self.linked_list.head.next
        return current_node.value

    def peek(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The stack is empty'
        return self.linked_list.head.value

    def delete_stack(self):  # TC O(1)
        self.linked_list.head = None
        return 'Successfully deleted the stack.'


custom_stack = Stack()
print(custom_stack)
print(custom_stack.is_empty())
print(custom_stack.push(1))
print(custom_stack.push(2))
print(custom_stack.push(3))
print(custom_stack)
print('------')
print(f'Removed element: {custom_stack.pop()}')
print(custom_stack)
print(f'Top element in the stack: {custom_stack.peek()}')
