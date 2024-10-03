# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array = []
        def order(array, root):
            if root: 
                order(array, root.left)
                order(array, root.right)
                array.append(root.val)
                
        order(array, root)
        return array