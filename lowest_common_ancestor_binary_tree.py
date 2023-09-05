from typing import Optional
from datatypes.binary_tree import TreeNode
from datatypes.binary_tree import list_to_binary_tree


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


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = find(root, p.val)
        path_q = find(root, q.val)
        lowest = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] != path_q[i]:
                break
            else:
                lowest = path_p[i]

        return lowest


if __name__ == '__main__':
    solution = Solution()
    tree = list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(solution.lowestCommonAncestor(tree, tree.find(2), tree.find(8)) == tree.find(6))
    print(solution.lowestCommonAncestor(tree, tree.find(2), tree.find(4)) == tree.find(2))