from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # Both None -> symmetric
            if not t1 and not t2:
                return True
            # One None, one not -> not symmetric
            if not t1 or not t2:
                return False
            # Values must match, and children must be mirrors
            return (
                t1.val == t2.val
                and isMirror(t1.left, t2.right)
                and isMirror(t1.right, t2.left)
            )

        return isMirror(root.left, root.right)
