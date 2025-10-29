# ============================================================
#  Basic Tree Node definition (used for all problems)
# ============================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1️⃣ Maximum Depth of Binary Tree
# ============================================================

class MaxDepthSolution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ============================================================
# 2️⃣ Invert Binary Tree
# ============================================================

class InvertTreeSolution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# ============================================================
# 3️⃣ Diameter of Binary Tree
# ============================================================

class DiameterSolution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter


# ============================================================
# 4️⃣ Same Tree
# ============================================================

class SameTreeSolution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ============================================================
# 5️⃣ Subtree of Another Tree
# ============================================================

class SubtreeSolution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        
        def same(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)

        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# ============================================================
# 6️⃣ Lowest Common Ancestor in BST
# ============================================================

class LCASolution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


# ============================================================
# 7️⃣ Binary Tree Level Order Traversal
# ============================================================

from collections import deque

class LevelOrderSolution:
    def levelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result


# ============================================================
# 8️⃣ Validate Binary Search Tree
# ============================================================

class ValidateBSTSolution:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float('-inf'), float('inf'))


# ============================================================
# 9️⃣ Kth Smallest Element in BST
# ============================================================

class KthSmallestSolution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans


# ============================================================
# 🔟 Serialize and Deserialize Binary Tree
# ============================================================

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        q = deque([root])
        result = []
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("N")
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        return root


# ============================================================
# ✅ Example usage (you can test each class separately)
# ============================================================

if __name__ == "__main__":
    # Example tree: [3,9,20,None,None,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print("1. Max Depth:", MaxDepthSolution().maxDepth(root))
    print("2. Level Order:", LevelOrderSolution().levelOrder(root))
    print("3. Diameter:", DiameterSolution().diameterOfBinaryTree(root))
    print("4. Validate BST:", ValidateBSTSolution().isValidBST(root))
