# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        temp = head
        while temp != None:
            temp = temp.next
            size +=1 

        target = size - n

        if target == 0:
            return head.next

        curr = head
        for _ in range(target - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head
        