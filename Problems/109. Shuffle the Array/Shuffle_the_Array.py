class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
                for i in range(n, 2*n):
            ans.append(nums[i-n])
            ans.append(nums[i])
                    return ans