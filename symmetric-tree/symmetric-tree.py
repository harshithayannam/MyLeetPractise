# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return true
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
            
        
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left))