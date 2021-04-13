class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])#sorting by end
        closingEnd = - float("inf")
        count = 0
        
        for start,end in intervals:
            if closingEnd <= start:
                closingEnd = end
            else:
                count += 1
        return count