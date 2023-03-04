"""
Binary tree made with Python list.
It will be with fixed size.
Initialize empty python list. The cell at index 0 is always empty.
We insert the root node at index 1. Based on that index we will calculate where to put
left and right child. The formula for calculating left child is cell(2*x); right child is cell(2*x + 1),
where x is the index of the root node.
"""


# Creation of binary tree with list.
class BinaryTree:
    def __init__(self, size):  # TC O(1) SC O(n)
        # Initialize empty list with the given size
        self.custom_list = [None] * size
        # The last index that we used
        self.last_used_index = 0
        self.size = size

    # Insert node in binary tree
    def insert_node(self, value):  # TC O(1) SC O(1)
        # Check if the size is reached
        if self.last_used_index + 1 == self.size:
            return 'The binary tree is full.'
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return f'The value {value} has been successfully inserted.'

    # Search for a node in binary tree.
    def search_node(self, searched_value):  # SC O(n) TC O(1)
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == searched_value:
                return f'The value {searched_value} was found in the binary tree.'
        return f'Node with value {searched_value} was not found in the binary tree.'

    # Pre order traversal
    def pre_order_traversal(self, index):  # TC O(n) SC O(n)
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(2 * index)
        self.pre_order_traversal((2 * index) + 1)

    def in_order_traversal(self, index):  # TC O(n) SC O(n)
        if index > self.last_used_index:
            return
        self.in_order_traversal(index * 2)
        print(self.custom_list[index])
        self.in_order_traversal(index * 2 + 1)

    def post_order_traversal(self, index):  # TC O(n) SC O(n)
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.custom_list[index])

    def level_order_traversal(self, index):  # TC O(n) SC O(1)
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    def delete_node(self, node_value):  # TC O(n) SC O(1)
        if self.last_used_index == 0:
            return 'The binary tree is empty.'
        for index in range(1, self.last_used_index + 1):
            if self.custom_list[index] == node_value:
                self.custom_list[index] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return f'Successfully deleted node {node_value}.'
        return 'No such node in the binary tree.'

    def delete_binary_tree(self):  # TC O(1) SC O(1)
        self.custom_list = None
        return 'Successfully deleted binary tree.'


binary_tree = BinaryTree(8)
print(binary_tree.insert_node('Drinks'))
print(binary_tree.insert_node('Hot'))
print(binary_tree.insert_node('Cold'))
print(binary_tree.insert_node('Tea'))
print(binary_tree.insert_node('Coffee'))

# print(binary_tree.search_node('Hot'))
binary_tree.level_order_traversal(1)
print('----')
print(binary_tree.delete_node('Hot'))
binary_tree.level_order_traversal(1)
