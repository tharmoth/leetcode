from datatypes.binary_tree import TreeNode
from datatypes.binary_tree import list_to_binary_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, q, p)
        if q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, q, p)
        return root


if __name__ == '__main__':
    solution = Solution()

    tree = list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(solution.lowestCommonAncestor(tree, tree.find(2), tree.find(8)) == tree.find(6))
    print(solution.lowestCommonAncestor(tree, tree.find(2), tree.find(4)) == tree.find(2))
