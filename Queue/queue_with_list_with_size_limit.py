"""
Queue with fixed capacity. Circular queue.
This way we fix the problem with the time complexity.
"""


class Queue:
    def __init__(self, max_size):  # TC O(1) SC O(n)
        # Creating python list with predefined None values.
        self.items = max_size * [None]
        self.max_size = max_size
        # Pointers to the last added element and the first element.
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(el) for el in self.items]
        return ' '.join(values)

    # Checking if the queue is already full.
    def is_full(self):  # TC O(1) SC O(1)
        # We don't have blank space between top and start.
        if self.top + 1 == self.start:
            return True
        if self.start == 0 and self.top + 1 == self.max_size:
            return True
        return False

    def is_empty(self):  # TC O(1) SC O(1)
        # If top is -1 this means that our queue is empty.
        if self.top == -1:
            return True
        return False

    def enqueue(self, value):  # TC O(1) SC O(1)
        if self.is_full():
            return 'The queue is full'
        # Our top element points to the last element.
        if self.top + 1 == self.max_size:
            self.top = 0
        else:
            self.top += 1
            # Checking if this will be the first element
            if self.start == -1:
                self.start = 0
        # Top points to the index of the last added element.
        self.items[self.top] = value
        return 'The element is inserted at the end of the queue.'

    def dequeue(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The queue is empty'
        first_element = self.items[self.start]
        start = self.start
        # If this is true it means we have only one element in the queue.
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.max_size:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element

    def peek(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The queue is empty'
        return self.items[self.start]

    def delete_queue(self):  # TC O(1) SC O(1)
        self.start = -1
        self.top = -1
        self.items = self.max_size * [None]
        return 'Successfully deleted queue.'


custom_queue = Queue(3)
print(custom_queue.is_full())
print(custom_queue.is_empty())
print(custom_queue.enqueue(1))
print(custom_queue.enqueue(2))
print(custom_queue.enqueue(3))
print(custom_queue)
print(custom_queue.is_full())
# print(custom_queue.enqueue(4))
print(custom_queue.dequeue())
print(custom_queue)
print(custom_queue.peek())
print(custom_queue.delete_queue())
print(custom_queue)
