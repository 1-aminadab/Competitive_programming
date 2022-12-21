class Solution(object):
    def merge(self, intervals):
        
        length = len(intervals)
        i = 0
        for i in range(length-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                intervals[i] = 0

        intervals[:] = (value for value in intervals if value != 0)
        return intervals
