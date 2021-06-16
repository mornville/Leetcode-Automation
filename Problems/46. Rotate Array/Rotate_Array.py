class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = length - k % length
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)
        self.reverse(nums, 0, length-1)
        def reverse(self, array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1