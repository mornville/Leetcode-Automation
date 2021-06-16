# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None
            def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                self.ans = root
            elif root.val > val:
                self.searchBST(root.left, val)
            else:
                self.searchBST(root.right, val)
        return self.ans