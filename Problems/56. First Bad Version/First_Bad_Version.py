# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n+1
                while low<=high:
            mid = (low+high)//2
                        if isBadVersion(mid) and mid-1>0:
                    if not isBadVersion(mid-1):
                        return mid
                    else:
                        high = mid-1
            elif not isBadVersion(mid) and mid+1<=n:
                if  isBadVersion(mid+1):
                    return mid+1
                else:
                    low = mid+1
            else:
                return 1
        return False