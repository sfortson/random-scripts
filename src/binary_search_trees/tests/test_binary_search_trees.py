import sys

import pytest

from src.binary_search_trees.binary_search_trees import (
    inorder_tree_walk,
    iterative_tree_search,
    tree_insert,
    tree_maximum,
    tree_minimum,
    tree_search,
    tree_successor,
)
from src.binary_search_trees.helpers import Node, Tree


def build_test_tree():
    root = Node(6)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right = Node(7)
    root.right.right = Node(8)

    return Tree(root)


T = build_test_tree()


class TestBinarySearchTrees:
    def test_inorder_tree_walk(self):
        inorder_tree_walk(T.root)
        assert True

    def test_tree_search(self):
        assert tree_search(T.root, 7).key == 7
        assert tree_search(T.root, 10) is None

    def test_iterative_tree_search(self):
        assert iterative_tree_search(T.root, 7).key == 7
        assert iterative_tree_search(T.root, 10) is None

    def test_min_max(self):
        assert tree_minimum(T.root).key == 2
        assert tree_maximum(T.root).key == 8

    def test_tree_successor(self):
        assert tree_successor(T.root).key == 7

    def test_tree_insert(self):
        new_node = Node(3)
        tree_insert(T, new_node)
        assert tree_search(T.root, 3).key == 3


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
