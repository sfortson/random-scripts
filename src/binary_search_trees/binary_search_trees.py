"""Binary search tree algorithms"""

def inorder_tree_walk(node):
    """Inorder tree walk

    :param node: node
    :type node: Node
    """
    if node is not None:
        inorder_tree_walk(node.left)
        print(node.key)
        inorder_tree_walk(node.right)


def tree_search(node, key):
    """Search in a tree

    :param node: Node
    :type node: Node
    :param k: _description_
    :type k: _type_
    :return: _description_
    :rtype: _type_
    """
    if node is None or key == node.key:
        return node
    if key < node.key:
        return tree_search(node.left, key)
    return tree_search(node.right, key)


def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


def tree_insert(tree, z):
    y = None
    x = tree.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        tree.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
