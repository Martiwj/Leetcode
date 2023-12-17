# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        data = []
        def postOrder(node):
            if node :
                data.append(str(node.val))
                postOrder(node.left)
                postOrder(node.right)
           
        postOrder(root)
        return ",".join(data)

    def deserialize(self, data):

        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(',')
      
        def insert(v, x):
            if v is None:
                return TreeNode(x)
            elif x < v.val:
                v.left = insert(v.left, x)
            elif x > v.val:
                v.right = insert(v.right, x)

            return v

        root = None
        for val in values:
        
            root = insert(root, int(val))

        return root
