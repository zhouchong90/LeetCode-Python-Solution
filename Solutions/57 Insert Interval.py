# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res, n = [], Interval(newInterval.start,newInterval.end)
        for i, intv in enumerate(intervals):
            if intv.end <  n.start:
                res.append(intv)
            elif intv.start >  n.end:
                res.append(n)
                res.extend(intervals[i:])
                return res
            else:
                n.start = min(intv.start, n.start)
                n.end = max(intv.end,n.end)
        res.append(n)
        return res
                