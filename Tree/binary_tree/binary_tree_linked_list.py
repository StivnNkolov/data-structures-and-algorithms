"""
Binary tree made with Link List.

"""
import queue_with_linked_list as queue


class TreeNode:
    def __init__(self, data):  # TC O(1) SC O(1)
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order_traversal(root_node):  # TC O(n) SC O(n)(because we are using stack memory.)
    """
    PreOrder traversal: visit the root, then the left subtree,
    then the right subtree.
    """
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):  # TC O(n) SC O(n)
    """
    InOrder traversal: First we visit the left subtree, then the root, then the right subtree.
    We start from the bottom left leaf.
    """
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):  # TC O(n) SC O(n)
    """
    PostOrder traversal: first visit the left subtree, then the right subtree, then root.
    """
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):  # TC O(n) SC O(n)
    """
    LevelOrder traversal: We visit each level of the tree, starting from the first level.
    """
    if not root_node:
        return
    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not (custom_queue.is_empty()):
        root = custom_queue.dequeue()
        print(root.value.data)

        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)

        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)


def search_in_tree(root_node, searched_value):  # TC O(n) SC O(n)
    """
    For searching in tree we always use level order traversal because queue perform
    better than stack.
    """
    if not root_node:
        return 'The binary tree does not exist.'

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.is_empty():
        current_node = custom_queue.dequeue()
        if current_node.value.data == searched_value:
            return f'The value {searched_value} exist in the tree.'
        if current_node.value.left_child is not None:
            custom_queue.enqueue(current_node.value.left_child)

        if current_node.value.right_child is not None:
            custom_queue.enqueue(current_node.value.right_child)

    return 'Value was not found in this tree.'


def insert_value(root_node, new_node):  # TC O(n) SC O(n)
    """
    Insert node in tree. Again we use level order traversal and search for empty place.
    """
    if not root_node:
        root_node = new_node
        return
    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.is_empty():
        current_node = custom_queue.dequeue()
        if current_node.value.left_child is not None:
            custom_queue.enqueue(current_node.value.left_child)
        else:
            current_node.value.left_child = new_node
            return f'Successfully inserted {new_node.data}'

        if current_node.value.right_child is not None:
            custom_queue.enqueue(current_node.value.right_child)
        else:
            current_node.value.right_child = new_node
            return f'Successfully inserted {new_node.data}'


def get_deepest_node(root_node):  # TC O(n) SC O(n)
    """
    Helper method to be used in deletion of node from the tree.
    Return the deepest node in th tree.
    """
    if not root_node:
        return
    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.is_empty():
        current_node = custom_queue.dequeue()

        if current_node.value.left_child is not None:
            custom_queue.enqueue(current_node.value.left_child)

        if current_node.value.right_child is not None:
            custom_queue.enqueue(current_node.value.right_child)

    return current_node.value


def delete_deepest_node(root_node, deepest_node):
    """
    Helper function for deleting node from tree.
    This func will delete the deepest node in the tree.
    """
    if not root_node:
        return

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.is_empty():
        current_node = custom_queue.dequeue()
        # Check if the current node is the deepest node. If so we set it to None.
        if current_node.value is deepest_node:
            current_node.value = None
            return
        """
        Here we check if any of the children of the current_node is the deepest node,
        we set it to None, otherwise we enqueue it to the queue.
        The only logic that I find behind that is that we save one iteration?
        """
        if current_node.value.right_child:
            if current_node.value.right_child is deepest_node:
                current_node.value.right_child = None
                return
            custom_queue.enqueue(current_node.value.right_child)

        if current_node.value.left_child:
            if current_node.value.left_child is deepest_node:
                current_node.value.left_child = None
                return
            custom_queue.enqueue(current_node.value.left_child)


def delete_node(root_node, node):  # TC O(n) SC O(n)
    """
    First we need to find the deepest node (the node that we reach last when we use levelOrderTraversal).
    Then we find the node that we want to delete, and replace it with the deepest node (this way we are not losing
    the children of the node that we want to delete). Last we delete the deepest node from the binary tree.
    This is deletion of node from the tree.
    """

    if not root_node:
        return

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.is_empty():
        current_node = custom_queue.dequeue()
        # Check if the current_node is the one that we want to delete.
        if current_node.value.data == node:
            # We find the deepest node in our tree.
            d_node = get_deepest_node(root_node)
            # We set the current node to the deepest node.
            current_node.value.data = d_node.data
            # Then we delete the deepest node.
            delete_deepest_node(root_node, d_node)
            return 'The node has been successfully deleted.'

        if current_node.value.left_child is not None:
            custom_queue.enqueue(current_node.value.left_child)

        if current_node.value.right_child is not None:
            custom_queue.enqueue(current_node.value.right_child)
    return 'There is no such node in the tree.'


def delete_binary_tree(root_node):  # TC O(1) SC O(1)
    """
    This way we destroy the connection between root and child nodes.
    Garbage collector will delete the rest of the nodes.
    """
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return 'Successfully deleted binary tree.'


# Set up
binary_tree = TreeNode('Drinks')
left_child = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
left_child.left_child = tea
left_child.right_child = coffee
right_child = TreeNode('Cold')
binary_tree.left_child = left_child
binary_tree.right_child = right_child

# pre_order_traversal(binary_tree)
# print('-----')
# in_order_traversal(binary_tree)
# print('-----')f
# post_order_traversal(binary_tree)
# print('-----')
level_order_traversal(binary_tree)
# # print('-----')
# # print(search_in_tree(binary_tree, 'Hot'))
# cola = TreeNode('Cola')
# print(insert_value(binary_tree, cola))
# print(delete_node(binary_tree, 'Hot'))
print('-----')
# level_order_traversal(binary_tree)
print(delete_binary_tree(binary_tree))
print('-----')
level_order_traversal(binary_tree)
