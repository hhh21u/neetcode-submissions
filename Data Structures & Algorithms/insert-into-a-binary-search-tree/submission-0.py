# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root

        node = root

        def dfs(node, val):
            if node is None:
                return TreeNode(val)
            if val > node.val:
                node.right = dfs(node.right, val)
            else:
                node.left = dfs(node.left, val)
            return node
        
        dfs(node, val) # 5, 6 # 6 < 9
        return root