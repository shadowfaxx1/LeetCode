class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root=None):
        self.root = root

    def createBT(self, values):
        def create_tree(index):
            if index >= len(values) or values[index] is None:
                return None

            root = Node(values[index])
            root.left = create_tree(2 * index + 1)
            root.right = create_tree(2 * index + 2)
            return root

        self.root = create_tree(0)

    def mindepth(self, root):
        # base case
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.mindepth(root.left) if root.left else float('inf')
        right = self.mindepth(root.right) if root.right else float('inf')
        return min(self.mindepth(root.left),self.mindepth(root.right)) + 1

values = [2, None, 3, None, 4, None, 5, None, 6]
s = Solution()
root = s.createBT(values)
print(s.mindepth(root))
