"""
Binary tree made with Link List.


"""


class TreeNode:
    def __init__(self, data):  # TC O(1) SC O(1)
        self.data = data
        self.left_child = None
        self.right_child = None


binary_tree = TreeNode('Drinks')
left_child = TreeNode('Hot')
right_child = TreeNode('Cold')
binary_tree.left_child = left_child
binary_tree.right_child = right_child


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


pre_order_traversal(binary_tree)
print('-----')
in_order_traversal(binary_tree)
