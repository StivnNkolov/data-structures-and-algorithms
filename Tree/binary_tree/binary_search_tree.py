"""
BST is basically binary tree but with more properties.
In the left subtree the value of a node is less than or equal to its parent node's value.
In the right subtree the value of a node is greater than its parent node's value.
BST does not store index of its data elements, instead it relies on implicit structure ti keep
a record of where each element is. Because of that it perform faster than Binary Tree when
inserting and deleting nodes.

We will create it with Linked List.
"""

import queue_with_linked_list as queue


class BinarySearchTreeNode:
    def __init__(self, data):  # TC O(1) SC O(1)
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):  # TC O(logN) SC O(logN)
    if root_node.data is None:
        root_node.data = node_value
        return f'Node {node_value} was successfully inserted as root node.'
    if node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BinarySearchTreeNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BinarySearchTreeNode(node_value)
        else:
            insert_node(root_node.right_child, node_value)
    return f'Node {node_value} was successfully inserted.'


def pre_order_traversal(root_node):  # TC O(n) SC O(n)
    if not root_node:
        return

    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):  # TC O(n) SC O(n)
    if not root_node:
        return

    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):  # TC O(n) SC O(n)
    if not root_node:
        return

    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):  # TC O(n) SC O(n)
    if not root_node:
        return

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.is_empty():
        current_node = custom_queue.dequeue()
        print(current_node.value.data)

        if current_node.value.left_child is not None:
            custom_queue.enqueue(current_node.value.left_child)

        if current_node.value.right_child is not None:
            custom_queue.enqueue(current_node.value.right_child)


def search_in_binary_tree(root_node, node_value):
    if root_node.data == node_value:
        return f'The value {node_value} was found'
    # Line 88 to 90 was added by me to fix the bug with element not found.
    if root_node.left_child is None and root_node.right_child is None:
        print('No such element')
        return

    if node_value <= root_node.data:
        if root_node.left_child.data == node_value:
            print('The value was found')
        else:
            search_in_binary_tree(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print('The value was found')
        else:
            search_in_binary_tree(root_node.right_child, node_value)


def search_in_binary_tree2(root_node, node_value):  # TC O(logN) SC O(logN)
    if root_node.data == node_value:
        return f'The value {node_value} was found'

    if node_value <= root_node.data:
        if root_node.left_child.data == node_value:
            return 'Value was found'
        else:
            search_in_binary_tree(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            return 'value was found'
        else:
            search_in_binary_tree(root_node.right_child, node_value)


"""
Successor in the BST is the smallest value in the right subtree.

"""


def minimum_value(bst_node):
    """
    Helper method to find the smallest value in the right subtree.
    bst_node is not the root node. It is actually the node that we want to start our loop from.
    We traverse the left subtree because the smallest node will always be the last node in the
    left subtree of the node that we started from.
    """
    current_node = bst_node
    while current_node.left_child is not None:
        current_node = current_node.left_child
    return current_node


def delete_node(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp_node = root_node.right_child
            root_node = None
            return temp_node
        if root_node.right_child is None:
            temp_node = root_node.left_child
            root_node = None
            return temp_node

        temp_node = minimum_value(root_node.right_child)
        root_node.data = temp_node.data
        root_node.right_child = delete_node(root_node.right_child, temp_node.data)
    return root_node


new_BST = BinarySearchTreeNode(None)
insert_node(new_BST, 70)
insert_node(new_BST, 50)
insert_node(new_BST, 90)
insert_node(new_BST, 30)
insert_node(new_BST, 60)
insert_node(new_BST, 80)
insert_node(new_BST, 100)
insert_node(new_BST, 20)
# insert_node(new_BST, 40)
level_order_traversal(new_BST)
print('-----')
delete_node(new_BST, 30)

# post_order_traversal(new_BST)
level_order_traversal(new_BST)
