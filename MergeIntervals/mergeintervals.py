# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda i:i.start)
        merged = []

        if(sorted_intervals):
            first = sorted_intervals.pop(0)
            while(sorted_intervals):
                operand = sorted_intervals.pop(0)
                if first.end >= operand.start:
                    first.end = max(operand.end, first.end)
                else:
                    merged.append(first)
                    first = operand
        
            merged.append(first)

        return merged

