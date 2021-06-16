class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
                sortedArray = [None]*(len1+len2)
        i, j, k = 0, 0, 0
                while i < len1 and j < len2:
            if nums1[i]<nums2[j]:
                sortedArray[k] = nums1[i]
                i+=1
                k+=1
            else:
                sortedArray[k] = nums2[j]
                j+=1
                k+=1
                while i < len1:
            sortedArray[k] = nums1[i]
            i+=1
            k+=1
                while j < len2:
            sortedArray[k] = nums2[j]
            j+=1
            k+=1
        if k % 2 != 0:
            return (sortedArray[int((k-1)/2)])
        else:
            return ((sortedArray[int((k-1)/2)]) + (sortedArray[int(k/2)])) / 2