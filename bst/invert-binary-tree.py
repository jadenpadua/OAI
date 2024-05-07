# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node):
        # base case when we traverse outside a leaf, return none
        if node is None:
            return None
        # swap left and right subtrees
        node.left, node.right = node.right, node.left
        # recurse into both subtrees up until we go outside of the leaves
        self.recurse(node.left)
        self.recurse(node.right)
        # return node once recursive swapping has finished
        return node
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recurse down and keep swapping until we get to a null node
        res = self.recurse(root)
        return res
