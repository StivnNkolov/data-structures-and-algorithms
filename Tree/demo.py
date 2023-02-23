"""
A tree is a nonlinear data structure with hierarchical relationships between its elements
without having any cycle. It is basically reversed from a real life tree.

Every time when we go one step down, it becomes more specialized form of its parent.
Every node has two components: data and reference to its sub category.
We have root node and under the root we have sub-nodes.

Tree data structure allow quicker, easier access to the data as it is nonlinear.
Store hierarchical data, like folder structure, XML/HTML data.

Tree terminology:
Root - node that don't have any parent. Top node.
Edge - a link between a parent and a child.
Leaf - a node which does not have a children.
Sibling - children of same parent.
Ancestor - parent, grandparent, great-grandparent of a node.
Depth of node - a length of the path from root to node. Calculating the number of edges.
Height of node - a length of the path from the node to the deepest node.
Depth of tree - depth of root node.
Height of tree - height of root node.

"""
