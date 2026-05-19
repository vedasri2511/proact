class Solution:
    def getMinimumDifference(self, root):
        prev = float('-inf')
        ans = float('inf')

        def inorder(node):
            nonlocal prev, ans
            if not node:
                return

            inorder(node.left)

            ans = min(ans, node.val - prev)
            prev = node.val

            inorder(node.right)

        inorder(root)
        return ans