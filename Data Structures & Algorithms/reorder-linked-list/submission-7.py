# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        curr = dummy
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        bro = slow
        slow = slow.next
        bro.next = None
        prev = None
        while slow:
            slowy = slow.next
            slow.next = prev
            prev = slow
            slow = slowy
        inty = 0
        while head and prev:
            if inty == 0:
                curr.next = head
                head = head.next
                inty += 1
                curr = curr.next
            else:
                curr.next = prev
                prev = prev.next
                inty -= 1
                curr = curr.next
        if head != None:
            curr.next=head
            

        