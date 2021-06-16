class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = len(nums) 
        i = 0
                while i< p1:
            if nums[i] == val:
                nums[i] = nums[p1-1]
                p1-=1
            else:
                i+=1
        return p1
                