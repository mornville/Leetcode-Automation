class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        orderdList = sorted(nums)
        sum = 0
        i=0
        while(i<len(orderdList)-1):
            sum+=min(orderdList[i], orderdList[i+1])
            i+=2
        return sum        