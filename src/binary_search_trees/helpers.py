class Tree:
    def __init__(self, root):
        self.root = root


class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.p = None
