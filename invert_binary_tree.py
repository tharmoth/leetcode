from typing import Optional
from datatypes.binary_tree import TreeNode
from datatypes.binary_tree import list_to_binary_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root

    def invertTreeOld(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            if node is not None:
                node.left, node.right = node.right, node.left
                nodes.append(node.left)
                nodes.append(node.right)

        return root


if __name__ == '__main__':
    solution = Solution()
    print(solution.invertTree(None) is None)
    print(solution.invertTree(list_to_binary_tree([4, 2, 7, 1, 3, 6, 9])) == list_to_binary_tree([4, 7, 2, 9, 6, 3, 1]))
    print(solution.invertTree(list_to_binary_tree([2, 1, 3])) == list_to_binary_tree([2, 3, 1]))
