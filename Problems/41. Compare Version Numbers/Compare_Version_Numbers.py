class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = version1.split(".")
        versions2 = version2.split(".")
        for i in range(max(len(versions1),len(versions2))):
            v1 = int(versions1[i]) if i < len(versions1) else 0
            v2 = int(versions2[i]) if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 <v2:
                return -1
        return 0
        