from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        

        modes = defaultdict(int)
        
        def wrapper(root):
            if root:
                modes[root.val] += 1
                wrapper(root.left)
                wrapper(root.right)
        
        wrapper(root)
        max_freq = max(modes.values(), default=0)
        return [val for val, freq in modes.items() if freq == max_freq]
        