
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
                
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def wrapper(root):
            if root:
        
                arr.append(root.val)
                root.right = wrapper(root.right)

        wrapper(root)
        return arr
        