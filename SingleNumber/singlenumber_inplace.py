class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for i in xrange(1, len(A)):
            A[0] = A[0] ^ A[i]
        return A[0]