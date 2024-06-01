# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        # base case, return true and depth of 0
        if not node: 
            return [True, 0]
        # call DFS recursively on subtrees
        left, right = self.dfs(node.left), self.dfs(node.right)
        # node is balanced if nodes in subtrees are balanced and height constraint is met
        is_balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
        # return T/F for higher up node to consume along with height of current node
        return [is_balanced, 1 + max(left[1], right[1])]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
