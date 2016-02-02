# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        
        out = []
        for i in sorted(intervals, key = lambda i:i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(i.end,out[-1].end)
            else:
                out.append(i)
        return out