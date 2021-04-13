from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #sort the list  
    intervals.sort(key=lambda x:x[0])

    # init the first ele
    res=[intervals[0]]

    #loop through the array expect the first

    for start,end in intervals[1:]:

        #last ele of the res and end intervel

        lastEnd =res[-1][1]
        # if timeline is in the range do it
        if start <= lastEnd:
            res[-1][1] = max(lastEnd,end)
        else:
            # res append
            res.append([start,end])
    return res