# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        A = []
        def inorder(root):
            if root:
                inorder(root.left)
                A.append(root.val)
                inorder(root.right)

        inorder(root)
        c = 0
        for i in A:
            if i >= low and i <= high:
                c += i
        return c
