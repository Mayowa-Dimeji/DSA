# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
from collections import deque


def connect(root):
    if not root:
        return root
    queue = deque([root])

    while queue:
        n = len(queue)
        next_pointer = None

        for i in range(n):
            node = queue.popleft()

            if next_pointer:
                next_pointer.next = node
            next_pointer = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        next_pointer.next = None
    return root
