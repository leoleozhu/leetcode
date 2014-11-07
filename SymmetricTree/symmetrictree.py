# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        arr=[root]
        while(len(arr)):
            if not self.isLayerSymmetric(arr):
                return False
            up = arr
            arr=[]
            for x in up:
                if x is not None:
                    arr.extend([x.left,x.right])

        return True

    def isLayerSymmetric(self, layer):
        l = len(layer)
        return all(self.eqNodes(layer[i],layer[l-i-1]) for i in xrange(l/2))

    def eqNodes(self, l, r):
        return (l is None and r is None) or (l is not None and r is not None and l.val==r.val)