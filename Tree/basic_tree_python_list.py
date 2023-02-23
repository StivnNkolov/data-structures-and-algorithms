"""
Basic tree using python list.
Unlimited children.
"""


class TreeNode:
    def __init__(self, data, children=[]):
        # The data of the node.
        self.data = data
        # The children of this node.
        self.children = children

    def __str__(self, level=0):
        result = '  ' * level + str(self.data) + '\n'
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def add_children(self, tree_node):
        self.children.append(tree_node)


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
print(tree)
tree.add_children(cold)
tree.add_children(hot)
print(tree)
coffee = TreeNode('Coffee', [])
tea = TreeNode('Tea', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.add_children(cola)
cold.add_children(fanta)
hot.add_children(coffee)
hot.add_children(tea)
print(tree)
