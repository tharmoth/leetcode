### Description

> Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
>
>According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

---
## Comparing Paths
### Method
My intuition in how to solve this was to find the path to each tree node and then compare the paths. You do this by implementing a find function that returns a list containing the nodes from the tree root to the given node. Then you iterate over the lists comparing the values and return the lowest common ancestor

### Complexity
Time Complexity - O(3n) - You iterate over the tree twice to find each node and then again to assess parentry.
Space Complexity - O(2n) You store the paths to each node

### Code
```py
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
```
### Problems in my solution
Both the space and time complexity of my solution is quite poor. I suspect a better answer exists. Perhaps multi purpose the find function to return both paths if you happen to find them. Or maybe do the comparison on the fly in the search function.

After looking at the solution:
Ahh, I didn't understand what a binary search tree was. This is sorted and therefore can be done in a single iteration.

Note: this is a (rather poor) solution to the general unsorted case

---
## Recursive Search
### Method
With the knowledge now in hand of how binary search trees are sorted I was able to property implement a far superior solution.

In a binary search tree values on the left must be 
- lower
- one of
	- A Binary Search Tree
	- None

and values on the right must be
- greater
- one of
	- A Binary Search Tree
	- None

So therefore we can recusively check if the node we are on is either grater or less then the nodes we are searching for and if it not either greater than or less than both values we have found the node we are searching for.

### Complexity
Time Complexity - O(n) in the worst case we could iterate through all nodes
Space Complexity - O(1) We only hold the current node in memory

### Code
```py
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
    if q.val < root.val and p.val < root.val:  
        return self.lowestCommonAncestor(root.left, q, p)  
    if q.val > root.val and p.val > root.val:  
        return self.lowestCommonAncestor(root.right, q, p)  
    return root
```

### Problems in my solution
We could simplify the if statements, but I do not believe it is worth the increased complexity. Though It may be better to one better versed in pythonic syntax.

---
### Links:

[Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:

#bianry-tree #search #binary-search-tree #binary-search