# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        x = 0
        if L <= root.val <= R:
            x = root.val
        if root.left is not None:
            x = x + self.rangeSumBST(root.left, L, R)
        if root.right is not None:
            x = x + self.rangeSumBST(root.right, L, R)
        return x




