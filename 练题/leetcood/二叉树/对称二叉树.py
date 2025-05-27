# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from turtle import TurtleGraphicsError
from typing import Optional
from unittest.mock import right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        if not root:
            return True
        return isMirror(root.left,root.right)
