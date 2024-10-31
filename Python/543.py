class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer=0

        def dfs(node):
            nonlocal answer

            if node==None:
                return 0
            
            left=dfs(node.left)
            right=dfs(node.right)

            answer=max(answer,left+right)
            return max(left,right)+1
        
        dfs(root)
        return answer