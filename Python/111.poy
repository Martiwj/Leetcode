# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0

        l_depth = self.minDepth(root.left)
        r_depth = self.minDepth(root.right)


        if not l_depth and not r_depth:
            return 1

    
        if not root.left:
            return 1 + r_depth

        if not r_depth:
            return 1 + l_depth
        
        return min(l_depth, r_depth) +1; 

        