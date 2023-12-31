from typing import Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(binary_tree_to_list(self))

    def __eq__(self, other):
        return isinstance(other, TreeNode) and self.val == other.val and self.left == other.left and self.right == other.right

    def find(self, value) -> Optional['TreeNode']:
        nodes = [self]
        while nodes:
            node = nodes.pop()
            if node:
                if node.val == value:
                    return node
                nodes.append(node.left)
                nodes.append(node.right)
        return None


def list_to_binary_tree(lst):
    """
    Convert a list to a binary tree.
    """
    if not lst:
        return None

    root = TreeNode(lst[0])
    nodes = [root]
    index = 1
    while index < len(lst):
        node = nodes.pop(0)
        if lst[index] is not None:
            node.left = TreeNode(lst[index])
            nodes.append(node.left)
        index += 1

        if index >= len(lst):
            break

        if lst[index] is not None:
            node.right = TreeNode(lst[index])
            nodes.append(node.right)
        index += 1

    return root


def binary_tree_to_list(root):
    """
    Convert a binary tree to a list.
    """
    result = []
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        if node:
            result.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)
        else:
            result.append(None)
    while result[-1] is None:
        result.pop()
    return result


def find(root, value) -> Optional[list]:
    nodes = [[root]]
    while nodes:
        node = nodes.pop()
        if node[-1]:
            if node[-1].val == value:
                return node

            a = node.copy()
            a.append(node[-1].left)
            nodes.append(a)
            b = node.copy()
            b.append(node[-1].right)
            nodes.append(b)
    return None