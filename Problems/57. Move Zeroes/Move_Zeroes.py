class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         for j in range(i+1, len(nums)):
        #             if nums[j] != 0:
        #                 nums[i] = nums[j]
        #                 nums[j] = 0
        #                 break
                x=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[x]=nums[i]
                x+=1
                while x!=len(nums):
            nums[x]=0
            x+=1