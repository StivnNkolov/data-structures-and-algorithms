class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                if current_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.head is None:
            print('The sll is empty')
            return
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def search_value(self, value):
        if self.head is None:
            return 'The sll is empty'
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == value:
                return f'The sll contains the value {value} at index {index}'
            current_node = current_node.next
            index += 1
        return f'Value {value} is not found'

    def delete_node(self, location):
        if self.head is None:
            print('SLL does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node_before_last_node = self.head
                    while node_before_last_node is not None:
                        if node_before_last_node.next == self.tail:
                            break
                        node_before_last_node = node_before_last_node.next
                    node_before_last_node.next = None
                    self.tail = node_before_last_node
            else:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node_before_the_node_we_want_to_delete = self.head
                    index = 0

                    while index < location - 1:
                        node_before_the_node_we_want_to_delete = node_before_the_node_we_want_to_delete.next
                        index += 1

                    node_we_want_to_delete = node_before_the_node_we_want_to_delete.next
                    node_before_the_node_we_want_to_delete.next = node_we_want_to_delete.next

    def delete_entire_sll(self):
        self.head = None
        self.tail = None


sll = SLL()
# node_1 = Node(1)
# node_2 = Node(2)

# sll.head = node_1
# sll.head.next = node_2
# sll.tail = node_2
# sll.insert(1, 1)
# sll.insert(2, -1)
# sll.insert(3, -1)
# sll.insert(4, -1)
# sll.insert(5, 1)
# sll.insert(6, 0)
# sll.insert(7, -1)
sll.traverse()
print([el.value for el in sll])
sll.delete_node(-1)
print([el.value for el in sll])
