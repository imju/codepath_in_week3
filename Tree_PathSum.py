# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def checkLeaf(self, node):
        if node.left is None and node.right is None:
            return True
        return False


    def checkPath(self, node, remain):
        result = remain - node.val
        if self.checkLeaf(node):
            if result == 0:
                return True
            return False

        if node.left != None:
            check_left = self.checkPath(node.left, result)
            if check_left :
                return True

        if node.right != None:
            check_right = self.checkPath(node.right, result)
            if check_right :
                return True

        return False





    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        return self.checkPath(A, B)
