"""
Create stack with minimum method. The method should return
the smallest value at any point. It must be O(1).
We implement it using Linked List.
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        # Same as head in LL
        self.top = None
        # Keeping the min value here.
        self.min_node = None

    def min(self):
        if not self.min_node:
            return None
        return self.min_node

    def push(self, value):
        if self.min_node and (self.min_node.value < value):
            self.min_node = Node(value=self.min_node.value, next=self.min_node)
        else:
            self.min_node = Node(value=value, next=self.min_node)
        self.top = Node(value=value, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.min_node = self.min_node.next
        item = self.top.value
        self.top = self.top.next
        return item


custom_stack = Stack()
custom_stack.push(5)
print(custom_stack.min())
custom_stack.push(6)
print(custom_stack.min())
custom_stack.push(3)
print(custom_stack.min())
custom_stack.pop()
print(custom_stack.min())
