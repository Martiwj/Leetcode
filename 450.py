# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def findMin(self, root):
        if root.left == None:
            return root

        return self.findMin(root.left)

    def deleteNode(self, root, key):
        if root == None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left == None:
            return root.right

        if root.right == None:
            return root.left
        
        u = self.findMin(root.right)
        root.val = u.val
        root.right = self.deleteNode(root.right, u.val)
        return root


       