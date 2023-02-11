"""
Creating stack, using python list, with size limit.
"""


class Stack:
    def __init__(self, max_size):  # TC O(1) SC O(1)
        self.list = []
        self.max_size = max_size

    def __str__(self):
        values = reversed(self.list)
        values = [str(el) for el in values]
        return '\n'.join(values)

    def is_empty(self):  # TC O(1) SC O(1)
        if self.list:
            return False
        return True

    # Method to check if we already reached the max size of the stack.
    def is_full(self):  # TC O(1) SC O(1)
        if len(self.list) == self.max_size:
            return True
        return False

    def push(self, value):  # TC amortized constant/O(1)/O(n^2) SC O(1)
        if self.is_full():
            return 'The stack is full'
        self.list.append(value)
        return f'The element {value} has been successfully inserted.'

    def pop(self):
        if self.is_empty():
            return 'The stack is empty'
        return self.list.pop()

    def peek(self):  # TC(1) SC O(1)
        if self.is_empty():
            return 'The stack is empty'
        return self.list[-1]

    def delete_stack(self):  # TC O(1) SC O(1)
        self.list = None
        return 'Successfully deleted the stack.'


custom_stack = Stack(2)
print(custom_stack.is_empty())
print((custom_stack.is_full()))
print(custom_stack.push(1))
print(custom_stack.push(1))
print(f'Is the stack full: {custom_stack.is_full()}')
print((custom_stack.push(2)))
print(custom_stack)
print('------')
print(custom_stack.pop())
