# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        node = root
        # replace with the right most leave of left or the left most leave of right
        target = None
        prev = None
        while node:
            if node is None:
                return root
            if node.val < key:
                prev = node
                node = node.right
            elif node.val > key:
                prev = node
                node = node.left
            else:
                target = node
                break
        if target is None:
            return root

        def insert(parent, node):
            if parent is None:
                return node
            if node.val > parent.val:
                parent.right = insert(parent.right, node)
            else:
                parent.left = insert(parent.left, node)
            return parent

        if prev is None: # root
            # insert right to left
            if target.left and target.right:
                insert(target.left, target.right)
                return target.left
            if target.right:
                return target.right
            return target.left
        
        elif prev.val < target.val: # right
            prev.right = None
        else: # left
            prev.left = None

        if target.left:
            insert(prev, target.left)
        if target.right:
            insert(prev, target.right)
        return root
        
            

