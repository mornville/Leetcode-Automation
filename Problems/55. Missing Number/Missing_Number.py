class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_sum = sum(nums)
        n = len(nums)
        actual_sum = n*(n+1)//2
        return actual_sum - missing_sum
            