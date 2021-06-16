class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
                        i = 0
        j = 0
        res = set()
        nums1.sort()
        nums2.sort()
        while( i < len(nums1) and j < len(nums2) ):
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
            res.add(nums1[i])
            i += 1
            j += 1
        return res