# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        bruh = l1
        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + carryover
            elif l1:
                value = l1.val + carryover
            elif l2:
                value = l2.val+ carryover
            carryover = value//10
            value = value%10
            if l1 == None:
                l1 = ListNode()
                prev.next = l1
                l1.val = value
            if l1:
                l1.val = value
                prev = l1
                l1 = l1.next
            if l2:
                l2.val = value
                prevy = l2
                l2 = l2.next
        if carryover>0:
            l1 = ListNode()
            prev.next = l1
            l1.val = carryover
        return bruh
        

            

        