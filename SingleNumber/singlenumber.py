class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d = {}
        for i in A:
            if i in d:
                del d[i]
            else:
                d[i]=None
        return d.keys()[0]