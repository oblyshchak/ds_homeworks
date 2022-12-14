import pytest
from tree import Tree

tree_list = [9, 5, 12, 3, 8, 10, 15]

class TestTree:

    def test_insert(self):
        result = []
        self.obj_tree = Tree(9)
        self.obj_tree.insert(5)
        self.obj_tree.insert(12)
        self.obj_tree.insert(3)
        self.obj_tree.insert(8)

        before_adding = self.obj_tree.print_inorder()
        self.obj_tree.insert(10)
        self.obj_tree.insert(15)

        after_adding = self.obj_tree.print_inorder()
        assert before_adding != after_adding



    def test_min(self):
        self.obj_tree = Tree(9)
        self.obj_tree.insert(5)
        self.obj_tree.insert(12)
        self.obj_tree.insert(3)
        self.obj_tree.insert(8)
        self.obj_tree.insert(10)
        self.obj_tree.insert(15)
        assert self.obj_tree.min_value() == 3

    def test_max(self):
        self.obj_tree = Tree(9)
        self.obj_tree.insert(5)
        self.obj_tree.insert(12)
        self.obj_tree.insert(3)
        self.obj_tree.insert(8)
        self.obj_tree.insert(10)
        self.obj_tree.insert(15)
        assert self.obj_tree.max_value() == 15

    def test_delete(self):
        self.obj_tree = Tree(9)
        self.obj_tree.insert(5)
        self.obj_tree.insert(12)
        self.obj_tree.insert(3)

        before_deleting = self.obj_tree.print_inorder()
        self.obj_tree.delete(5)
        after_deleting = self.obj_tree.print_inorder()
        assert before_deleting != after_deleting
