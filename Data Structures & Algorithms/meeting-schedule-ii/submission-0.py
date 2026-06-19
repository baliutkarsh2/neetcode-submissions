"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for i in intervals:
            times.append((i.start, 1))
            times.append((i.end, -1))
        
        times.sort(key = lambda a : (a[0], a[1]))
        count = 0
        ret = 0
        for time in times:
            count += time[1]
            ret = max(ret, count)
        return ret
            

        