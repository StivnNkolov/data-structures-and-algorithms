"""
Queue is a data structure that stores items in First-in/First-out manner. FIFO
The first element that go into our queue will be the first element to get out.
A new addition to this queue happens at the end of the queue.
"""

"""
This implementation may be very time consuming, because of the automatic relocation
that is happening in the python list.
"""


class Queue:
    def __init__(self):  # TC O(1) SC O(1)
        self.items = []

    def __str__(self):
        values = [str(el) for el in self.items]
        return ' '.join(values)

    def is_empty(self):  # TC O(1) SC O(1)
        if self.items:
            return False
        return True

    # Add element to the queue
    def enqueue(self, value):  # TC O(n)(amortized constant) SC O(1)
        self.items.append(value)
        return f'The element {value} has been successfully inserted.'

    # Remove first element and return it.
    def dequeue(self):  # TC O(n) SC O(1)
        if self.is_empty():
            return 'The queue is empty.'
        return self.items.pop(0)

    # Return the first element
    def peek(self):  # TC O(1) SC O(1)
        if self.is_empty():
            return 'The queue is empty.'
        return self.items[0]

    def delete_queue(self):  # TC O(1) SC O(1)
        self.items = None
        return 'Successfully deleted the queue.'


custom_q = Queue()
print(custom_q.is_empty())
print(custom_q.enqueue(1))
print(custom_q.enqueue(2))
print(custom_q.enqueue(3))
print(custom_q)
print(f'Removed element: {custom_q.dequeue()}')
print(custom_q)
print(f'The first element is: {custom_q.peek()}')
print(custom_q.delete_queue())
