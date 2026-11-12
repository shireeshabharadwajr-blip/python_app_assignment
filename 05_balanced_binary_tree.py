class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    def height(node):
        if not node: return 0
        left = height(node.left)
        if left == -1: return -1
        right = height(node.right)
        if right == -1: return -1
        if abs(left - right) > 1: return -1
        return max(left, right) + 1
    return height(root) != -1

if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Example 1:", isBalanced(root1))
    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    print("Example 2:", isBalanced(root2))
