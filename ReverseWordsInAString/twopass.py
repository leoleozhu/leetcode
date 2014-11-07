class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        l = reversed([x for x in s.split(' ') if x])
        return ' '.join(l)

