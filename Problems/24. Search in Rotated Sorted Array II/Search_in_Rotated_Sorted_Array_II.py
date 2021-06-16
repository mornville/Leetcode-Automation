class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
                left, right = 0, len(nums)
                while left < right:
            mid = left + (right-left)//2
                        if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right  = mid
        return False
            