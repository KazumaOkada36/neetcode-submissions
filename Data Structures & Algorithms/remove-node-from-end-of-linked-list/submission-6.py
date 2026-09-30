# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        a = 0
        curr = dummy
        john = head
        while head:
            a += 1
            head = head.next
                
        j = a - n
        while curr and j != 0:
            j -= 1
            prev = curr
            curr = curr.next
        curr.next = curr.next.next

        return dummy.next


        
        
        

        