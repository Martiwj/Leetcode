class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        
        def preOrder(root, path):
            if root is None:
                return
            path += str(root.val)
            if root.left is None and root.right is None:
                paths.append(path)
            else:
                path += "->"
                preOrder(root.left, path)
                preOrder(root.right, path)
        
        preOrder(root, "")
        return paths
