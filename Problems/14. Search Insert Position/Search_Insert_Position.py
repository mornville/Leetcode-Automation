class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)