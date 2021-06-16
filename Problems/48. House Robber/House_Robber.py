class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                prev, cur = 0, 0
        for house in nums:
            cur, prev = max(prev + house, cur), cur
        return cur