class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        a = sorted(heights)
        count = 0
        for idx, element in enumerate(a):
            if element!=heights[idx]:
                count+=1
        return(count)