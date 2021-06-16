class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = (collections.Counter(nums))
        ans = 0
                for count in total.values():
            ans+= (count*(count-1)) // 2
                return ans