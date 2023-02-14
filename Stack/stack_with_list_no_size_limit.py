"""
Stack is a data structure that stores items in a Last-in/Last-out manner.
The last element added to the stack is the first one to be removed.
Example: browser back button.
Every time when we insert an element in the stack, the element will be
located on top of the previous element.
When we want to use LIFO functionality it is best to use Stack.
The chance of data corruption is minimum.
The biggest problem with stack is that the random access is not possible.
"""

"""
Creating stack, using python list, without size limit.
In this case we may have performance leaks as the size grows.
"""


class Stack:
    def __init__(self):  # Creating empty stack. TC O(1) SC O(1)
        self.list = []

    # making our stack more viewer friendly
    def __str__(self):
        # Reverse the order of the elements.
        values = reversed(self.list)
        # Making the values as str so that we can join them.
        values = [str(el) for el in values]
        # returning the elements in stacked way.
        return '\n'.join(values)

    # Check if we have any elements in the stack.
    def is_empty(self):  # TC O(1) SC O(1)
        if self.list:
            return False
        return True

    # Add element to the end of the stack
    def push(self, value):  # TC amortized constant/O(1)/O(n^2) SC O(1)
        self.list.append(value)
        return f'The element {value} has been successfully inserted.'

    # Removes and return the last element in the stack.
    def pop(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The stack is empty.'
        return self.list.pop()

    # Return the last element in the stack.
    def peek(self):  # TC(1) SC O(1)
        if self.is_empty():
            return 'The stack is empty'
        return self.list[-1]

    # Delete the entire stack.
    def delete_stack(self):  # TC O(1) SC O(1)
        self.list = None
        return 'Successfully deleted the stack.'


custom_stack = Stack()
print(custom_stack.is_empty())
print(custom_stack.push(1))
print(custom_stack.push(2))
print(custom_stack.push(3))

print(custom_stack)
print(f'Removed element: {custom_stack.pop()}')
print('-----')
print(custom_stack)
print('-----')
print(custom_stack.peek())
