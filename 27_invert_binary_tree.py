class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    inv = invertTree(root)
    print("Inverted root children:", inv.left.val, inv.right.val)
