from typing import Optional
from datatypes.binary_tree import TreeNode
from datatypes.binary_tree import list_to_binary_tree
from datatypes.binary_tree import binary_tree_to_list


class Solution:
    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left = self.height(root.left)
        if left <= -1:
            return -1

        right = self.height(root.right)
        if right <= -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0

    def isBalancedButWrong(self, root: Optional[TreeNode]) -> bool:
        nodes = [root]
        result = []
        depth_size = 1
        while nodes:
            node = nodes.pop(0)
            if node:
                result.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                result.append(None)

            if len(result) == depth_size + depth_size * 2:
                null_found = False
                for i in range(depth_size):
                    if not result or result.pop(0) is None:
                        null_found = True
                if null_found and not all(item is None for item in result):
                    return False
                depth_size *= 2

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBalanced(None) is True)
    print(solution.isBalanced(list_to_binary_tree([3, 9, 20, None, None, 15, 7])) is True)
    print(solution.isBalanced(list_to_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False)
    print(solution.isBalanced(list_to_binary_tree([1, 2, 3, 4, 5, 6, None, 8])) is True)
