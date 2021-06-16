class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = max(nums), sum(nums)
                while left<right:
            mid = left + (right-left) // 2
            if self.isValid(mid, nums, m):
                right = mid
            else:
                left = mid+1
                    return left
        def isValid(self, max, nums, m):
        sum = 0
        no_of_partition = 1
        start = 0
        while start < len(nums):
            sum+=nums[start]
            if sum>max:
                sum = nums[start]
                no_of_partition+=1                
                if no_of_partition > m:
                    return False
            start+=1            
        return True
        