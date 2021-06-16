class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        if(len(nums1)<len(nums2)):
            length = len(nums1)
            small = nums1
            big = nums2
        else:
            length = len(nums2)
            small = nums2
            big = nums1
        for i in range(0, length):
            for j in range(0, len(big)):
                if(small[i] == big[j]):
                    ans.append(small[i])
                    big[j] = -1
                    break
        return ans