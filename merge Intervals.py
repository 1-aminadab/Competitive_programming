class Solution(object):
    def merge(self, intervals):
        
       
        length = len(intervals)
        i = 0
        for j in range(len(intervals)):
            for k in range(len(intervals)-1):
                if intervals[k][0] > intervals[k+1][0]:
                    intervals[k], intervals[k+1] =intervals[k+1], intervals[k]

        for i in range(length-1):
            if intervals[i+1][0] <= intervals[i][1]:
                
                if intervals[i+1][1] <= intervals[i][1]:
                    intervals[i + 1][1] = intervals[i][1]
                intervals[i + 1][0] = intervals[i][0]
                intervals[i] = 0
        intervals[:] = (value for value in intervals if value != 0)
        return intervals
