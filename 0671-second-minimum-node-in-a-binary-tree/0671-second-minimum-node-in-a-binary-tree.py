class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minimum = root.val
        second = float("inf")

        def dfs(node):
            nonlocal second

            if not node:
                return

            if minimum < node.val < second:
                second = node.val
            elif node.val == minimum:
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return second if second != float("inf") else -1