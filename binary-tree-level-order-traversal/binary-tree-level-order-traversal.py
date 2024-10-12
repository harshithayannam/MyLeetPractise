# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.appendLis(root, 0, result)
        return result
    
    def appendLis(self, node: Optional[TreeNode], level: int, result: List[List[int]]):
        if not node:
            return 
        
        if level>=len(result):
            result.append([])
        
        result[level].append(node.val)
        
        self.appendLis(node.left, level + 1, result)
        self.appendLis(node.right, level + 1, result)