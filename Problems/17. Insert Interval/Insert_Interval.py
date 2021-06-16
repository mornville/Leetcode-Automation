class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        idx = -1
                for idx, (x,y) in enumerate(intervals):
            if y < newInterval[0]:
                ans.append([x,y])
            elif newInterval[1] < x:
                idx-=1
                break
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
                return ans + [newInterval] + intervals[idx+1:]