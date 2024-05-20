# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recurse(self, node, p, q, res=None) -> 'TreeNode':
        # Continue recursion as long as both p,q are on same subtrees and not node.val
        if p.val < node.val and q.val < node.val:
            return self.recurse(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.recurse(node.right, p, q)
        # Case where p,q does NOT reside in same subtree or one is node.val so return
        return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = self.recurse(root, p, q, None)
        return lca
