# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        n = 0
        def fdepth(root):
            if not root:
                return 0

            m = max(fdepth(root.left)+1,fdepth(root.right)+1)  

            return m  
        n = fdepth(root)
        return n 