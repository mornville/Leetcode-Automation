# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        totalLists = len(lists)
        interval = 1   
                while interval < totalLists:
            for i in range(0, totalLists-interval, interval*2):
                lists[i] = self.mergeLists(lists[i], lists[i+interval])
            interval = interval*2 
                    return lists[0]
        def mergeLists(self, list1, list2):
        head = temp = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list1
                list1 = temp.next.next
            temp = temp.next
                    if not list1:
            temp.next = list2
        else:
            temp.next = list1    
                    return head.next               