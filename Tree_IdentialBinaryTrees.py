# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def traverse(self, tree_node, node_list):

        if tree_node is None:
            return node_list

        if tree_node.left != None:
            node_list = self.traverse(tree_node.left, node_list)

        node_list.append(tree_node)

        if tree_node.right != None:
            node_list = self.traverse(tree_node.right, node_list)

        return node_list

    # build a stack from tree A then traverse the tree B in order fashion
    # B if tree B has more nodes or not matching then it is False
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        list_a = []
        list_b = []
        list_a = self.traverse(A,list_a)
        list_b = self.traverse(B,list_b)

        #print('list_a:'+str(list_a))
        #print('list_b:'+str(list_b))

        if len(list_a) != len(list_b):
            return False

        for i in range(len(list_a)):
            if list_a[i].val == list_b[i].val:
                continue
            else:
                return False

        return True
