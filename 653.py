# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        A = []
        def Inorder(v):
            if v:
                Inorder(v.left)
                A.append(v.val)
                Inorder(v.right)

        Inorder(root)

        maps = set()  
        for num in A:
            if k - num in maps:
                return True
            maps.add(num)
        return False