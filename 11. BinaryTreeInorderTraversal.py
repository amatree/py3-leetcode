# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if root is None: return []
        if root.left is None and root.right is None: return [root.val]
        
        result = []
        # get leftmost node
        leftmost = root
        left_nodes = []
        while leftmost.left is not None:
            leftmost = leftmost.left
            left_nodes.insert(0, leftmost)
        
        if leftmost.right is not None:
            left_nodes.insert(1, leftmost.right)
        left_nodes.append(root)
        
        # get rightmost node
        rightmost = root
        right_nodes = []
        while rightmost.right is not None:
            rightmost = rightmost.right
            right_nodes.insert(0, rightmost)
        
        if rightmost.left is not None:
            rightmost = rightmost.left
            right_nodes.insert(0, rightmost)
        
        for i in left_nodes:
            print(f"Left = {i.val}")
        for i in right_nodes:
            print(f"Right = {i.val}")
            
        print()
        
        # inorder traverse
        traverse = leftmost       
        while traverse != rightmost:
            print("current: ", traverse.val)
            if traverse == root:
                result.append(traverse.val)
                traverse = traverse.right
                continue
            if traverse.left is not None:
                result.append(traverse.left.val)
            elif traverse.right is not None:
                result.append(traverse.right.val)
            else:
                result.append(traverse.val)
            
            if len(left_nodes) > 1:
                traverse = left_nodes.pop(1)
            elif len(right_nodes) > 1:
                traverse = right_nodes.pop(1)
            else:
                break
            
        result.append(right_nodes[-1].val)
        return result
    
s = Solution()
test = TreeNode(52, left=TreeNode(40, left=TreeNode(24, right=TreeNode(32))), right=TreeNode(62, left=TreeNode(58), right=TreeNode(69)))
# 24, 32, 40, 52, 58, 62, 69
test2 = TreeNode(1, left=TreeNode(4), right=TreeNode(2, left=TreeNode(3)))
# 4 1 3 2

a = s.inorderTraversal(test)
print(a)