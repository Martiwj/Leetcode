# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
  
        if not l1 and not l2 and carry == 0:
            return None

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

      
        _sum = x + y + carry
        new_carry = _sum // 10
        current_digit = _sum % 10


        result_node = ListNode(current_digit)

        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        result_node.next = self.addTwoNumbers(next_l1, next_l2, new_carry)

        return result_node

