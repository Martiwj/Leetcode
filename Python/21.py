# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
          
        head = ListNode()
        current = head
        
        p1 = list1
        p2 = list2

        while p1 and p2:

            if p1.val < p2.val:
                current.next = ListNode(p1.val)
                p1 = p1.next
            else:
                current.next = ListNode(p2.val)
                p2 = p2.next

            current = current.next

        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        return head.next        