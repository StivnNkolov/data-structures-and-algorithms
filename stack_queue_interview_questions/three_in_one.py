"""
Use a single python list to create three stacks.
This is stack with limited size.
"""


class MultyStack:
    # Stack_size is the size limit for every stack in our list.
    def __init__(self, stack_size):
        # This is the number of stacks, we need to create from our list by definition.
        self.number_of_stacks = 3
        """
        Here we create our custom list, from whom we are going to create the 3
        stacks. We are creating a python list filled with zeros.
        The number of elements is determined from the number of stacks * the size
        of every single stack.
        """
        self.custom_list = [0] * (self.number_of_stacks * stack_size)
        """
        Here we create helper list that will contain the size of every single stack.
        In this list we have elements equal to the number of stacks and every element
        is representing the size of the stack.
        When we push element we += 1 to the value corresponding to the given stack
        and when we pop element we -= 1. This way we keep track if our stacks are full
        or not.
        """
        self.stacks_sizes = [0] * stack_size
        # This is the size for single stack in our list.
        self.stack_size = stack_size

    # Stack number is parameter that points to the stack we want to work with.
    def is_full(self, stack_number):
        """
        stack_sizes[stack_number] = the size of the stack we want to check.
        stack_sizes holds the size for all the stacks. We check the stack's
        size with this stack_number if it is equal to the stack_size we have
        from the initialization.
        """
        if self.stacks_sizes[stack_number] == self.stack_size:
            return True
        return False

    def is_empty(self, stack_number):
        # If the size of the stack we are checking is zero it means it is empty.
        if self.stacks_sizes[stack_number] == 0:
            return True
        return False

    # This is helper method that will return the last added element based on stack_number.
    # This method is doing all the magic for us.
    def top_element_index(self, stack_number):
        offset = stack_number * self.stack_size
        return offset + self.stacks_sizes[stack_number] - 1

    def push(self, value, stack_number):
        if self.is_full(stack_number):
            return 'The stack is full.'
        # This must happen first because on line 62 we are using this index!!
        # Increasing the size of this stack with one because we added element.
        self.stacks_sizes[stack_number] += 1
        # Changing the current top element with the new one.
        self.custom_list[self.top_element_index(stack_number)] = value
        return f'Successfully added {value} to stack with number {stack_number}'

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return 'The stack is empty.'
        # Taking the top value.
        value = self.custom_list[self.top_element_index(stack_number)]
        # Setting the top element in the current stack to 0
        self.custom_list[self.top_element_index(stack_number)] = 0
        # Reducing the size for this stack with one.
        self.stacks_sizes[stack_number] -= 1
        return value

    # Here we just return the top value in the desired stack.
    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return 'The stack is empty.'
        return self.custom_list[self.top_element_index(stack_number)]


custom_stack = MultyStack(6)
print(custom_stack.is_full(0))
print(custom_stack.is_empty(1))
print(custom_stack.push(1, 0))
print(custom_stack.push(2, 0))
print(custom_stack.push(3, 2))
print(custom_stack.pop(0))
print(custom_stack.custom_list)
