"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashy = {}
        dummy = Node(0)
        curr = dummy
        lol = head
        while head:
            curr.next = Node(0)
            curr = curr.next
            curr.val = head.val
            now = curr
            hashy[head] = now
            head = head.next
        while lol:
            nodey = hashy[lol]
            bruh = lol.random
            if bruh == None:
                nodey.random = None
            else:
                bro = hashy[bruh]
                nodey.random = bro
            lol = lol.next
        
        return dummy.next

        