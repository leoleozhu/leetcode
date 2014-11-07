class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {num[i]: i for i in xrange(len(num))}
        for i in xrange(len(num)):
            req = target-num[i]
            if req in d and i != d[req]:
                return (i+1, d[req]+1)
                
