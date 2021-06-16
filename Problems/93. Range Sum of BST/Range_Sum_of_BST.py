# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val >= low and root.val <= high:
                self.sum+=root.val
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
        return self.sum