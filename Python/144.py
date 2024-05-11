# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []

        def order(a,root):

            if root:
                a.append(root.val)
                order(a,root.left)
                order(a, root.right)
        
        order(a, root)
        return a