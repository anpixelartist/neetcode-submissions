# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        m = -1

        def fdepth(root):
            if not root:
                return 0
            depth = max(fdepth(root.right),fdepth(root.left)) +1  
            return depth


        def fun(root): 
            nonlocal m   
            if not root:
                return 

            m= max(fdepth(root.left)+fdepth(root.right) , m)

            fun(root.right)
            fun(root.left)
            return m

        return fun(root)    