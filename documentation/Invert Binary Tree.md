### Description

> Given the `root` of a binary tree, invert the tree, and return _its root_.
---
## Binary Tree Stack
### Method
In order to invert the tree have a stack of nodes which you initalize with the root node. While the stack contains nodes pop the top element off of the stack, invert it, and and it's children to the stack and continue. Do this until the entire tree is inverted.

### Complexity
Time Complexity - O(n) This involves iterating over each node so it scales with n
Space Complexity - O(n) in a imbalanced tree many nodes may get stuck in the stack

### Code
```py
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
    nodes = [root]  
    while nodes:  
        node = nodes.pop(0)  
        if node is not None:  
            node.left, node.right = node.right, node.left  
            nodes.append(node.left)  
            nodes.append(node.right)  
  
    return root
```
### Problems in my solution
It's space complexity is higher than average, there are probably some tricks that could be used to reduce it. A recursive solution may hold less data in memory for example

## Recursive Method
### Method
I decided to go ahead and implement the recursive method to see how it compares. It substantially reduced the code complexity along with memory usage, but increased runtime.

### Complexity
Time Complexity - O(n) it still traverses each node
Space Complexity - O(n) it still holds the parent nodes in memory

### Code
```py
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
    if root is not None:  
        root.left, root.right = root.right, root.left  
        self.invertTree(root.left)  
        self.invertTree(root.right)  
  
    return root
```

---
### Links:

[Leetcode](https://leetcode.com/problems/invert-binary-tree/)
[Github](https://github.com/tharmoth/leetcode)

### Tags:
#binary-tree #tree

