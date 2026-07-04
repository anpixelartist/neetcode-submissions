# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        max_diameter = 0

        # 2. Define a helper function that calculates depth AND updates the diameter
        def get_depth(node):
            nonlocal max_diameter
            if not node:
                return 0
            
            # Recurse down to find the maximum depth of left and right subtrees
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            
            # Update the global maximum diameter if the path through this 
            # current node is wider than any path found so far
            max_diameter = max(max_diameter, left_depth + right_depth)
            
            # Return the depth of the current node to its parent caller
            return max(left_depth, right_depth) + 1

        # 3. Kick off the recursive depth function starting at the root
        get_depth(root)
        
        # 4. Return the maximum diameter tracked during the traversal
        return max_diameter 