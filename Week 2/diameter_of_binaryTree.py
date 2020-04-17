'''
  Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    
    def traverse(self, root):
        if not root: return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.traverse(root)
        return self.ans

class Solution2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        d = {None: -1}
        s = [root]
        ans = 0
        while s:
            node = s[-1]
            if node.left in d and node.right in d:
                s.pop()
                l = d[node.left] + 1
                r = d[node.right] + 1
                ans = max(ans, l + r)
                d[node] = max(l, r)
            else:
                if node.left: s.append(node.left)
                if node.right: s.append(node.right)
        return ans

class Solution3:
    def depth(self, root):
        if not root: return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def traverse(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.depth(root.left) + 1 + self.depth(root.right), \
                           self.traverse(root.left), \
                           self.traverse(root.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.traverse(root) - 1, 0)

class Solution4:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = -1

        def diameter(root):
            if root is None:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            length = left + right + 1
            self.result = max(self.result, length)
            return max(left, right) + 1

        diameter(root)

        return 0 if self.result == -1 else self.result - 1
