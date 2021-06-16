# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def sumRootToLeaf(self, root: TreeNode) -> int:
        leafSum = 0
        stack = [(root, 0)]
                while stack:
            root, currSum = stack.pop()
            if root is not None:
                currSum = (currSum<<1) | root.val
                if root.left is None and root.right is None:
                    leafSum+=currSum
                else:
                    stack.append((root.right, currSum))
                    stack.append((root.left, currSum))
        return leafSum