# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        count = 1

        while queue:
            n = len(queue)
            level = []

            for _ in range(n):
                if count % 2 != 0:
                    node = queue.popleft()
                    if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if count % 2 == 0:
                    node = queue.pop()
                    if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)

            ans.append(level)
            count += 1
        return ans
