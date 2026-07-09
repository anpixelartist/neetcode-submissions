# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not root: 
            return False  # Main tree is empty, subRoot cannot be found
        
        # If trees match starting at current node, return True
        if self.isSameTree(root, subRoot):
            return True
            
        # Otherwise, search in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are empty
        if not p and not q:
            return True
        # One is empty, or values don't match
        if not p or not q or p.val != q.val:
            return False
            
        # Check both subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
