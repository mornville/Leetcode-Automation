class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]        """
        length = len(nums)
        ans = []
        for i in range(0, length):
            for j in range(i, length):                
                if(nums[i] + nums[j] == target):
                    if(i!=j):
                        ans.append(i)
                        ans.append(j)
        return ans
                